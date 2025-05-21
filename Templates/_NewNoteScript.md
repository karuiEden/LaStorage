<%*
// Запрос имени файла у пользователя
let newFileName = await tp.system.prompt("Введите имя новой заметки");

// Если пользователь отменил ввод (нажал Esc или оставил пустым), прекращаем выполнение скрипта
if (!newFileName) {
    new Notice("Создание заметки отменено.");
    return;
}

// Получаем текущую активную заметку
let currentFile = tp.file.current_file();

// Добавляем расширение .md, если оно отсутствует
if (!newFileName.endsWith(".md")) {
    newFileName += ".md";
}

// Переименовываем текущую заметку на основе введенного имени
try {
    await app.fileManager.renameFile(currentFile, newFileName);
} catch (e) {
    new Notice(`Ошибка при переименовании файла: ${e.message}`);
    return;
}

// Читаем содержимое вашего основного шаблона (Default.md)
// Убедитесь, что путь "Templates/Default.md" правильный для вашей установки
const templatePath = "Templates/Default.md"; // <-- Проверьте этот путь!
let defaultTemplateContent;
try {
    const templateFile = app.vault.getAbstractFileByPath(templatePath);
    if (!templateFile) {
        new Notice(`Шаблон по пути "${templatePath}" не найден.`);
        return;
    }
    defaultTemplateContent = await app.vault.read(templateFile);
} catch (e) {
    new Notice(`Ошибка при чтении шаблона: ${e.message}`);
    return;
}

// Имя файла без расширения для использования в заголовке
let titleForContent = newFileName.replace(/\.md$/, '');

// Заменяем <% tp.file.title %> на введенное имя файла в содержимом шаблона
let processedContent = defaultTemplateContent.replace(/<%\\s*tp\\.file\\.title\\s*%>/g, titleForContent);

// Обрабатываем другие Templater-переменные (например, tp.date.now()) в шаблоне Default.md
processedContent = await tp.eta.compile(processedContent)(tp);

// Вставляем модифицированный шаблон в текущий файл
await tp.editor.insertContent(processedContent);

// Опционально: переместить курсор в нужное место
let contentLines = processedContent.split('\n');
let cursorLine = -1;
for (let i = 0; i < contentLines.length; i++) {
    if (contentLines[i].trim().startsWith('# ' + titleForContent)) {
        cursorLine = i + 2; // +1 для перехода на следующую строку, +1 для пропуска пустой строки после заголовка
        break;
    }
}
if (cursorLine !== -1) {
    await tp.editor.cursor.set(cursorLine);
}
_%>
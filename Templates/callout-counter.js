module.exports = async (tp) => {
  // Названия всех типов callout и их счётчики
  const counters = { theorem: 0, definition: 0, lemma: 0, proof: 0, proposition: 0, remark: 0 };

  // Функция для нумерации callout-блоков
  const renumberCallouts = () => {
    document.querySelectorAll(".callout").forEach(callout => {
      const type = callout.dataset.callout;
      if (!type || counters[type] === undefined) return;

      // Инкремент только если ещё не пронумеровано
      const title = callout.querySelector(".callout-title-inner") || callout.querySelector(".callout-title");

      if (!title) return;

      // Проверяем, пронумерован ли уже блок
      if (!title.dataset.numbered) {
        counters[type]++;
        let label = "";
        switch(type) {
          case "theorem": label = "Теорема"; break;
          case "definition": label = "Определение"; break;
          case "lemma": label = "Лемма"; break;
          case "proof": label = "Доказательство"; break;
          case "proposition": label = "Утверждение"; break;
          case "remark": label = "Замечание"; break;
        }

        title.textContent = `${label} ${counters[type]}. ${title.textContent}`;
        title.dataset.numbered = "true";
      }
    });
  };

  // Первый проход после загрузки заметки
  renumberCallouts();

  // MutationObserver для динамического обновления при ререндере блоков (виртуализация Preview)
  const observer = new MutationObserver(renumberCallouts);
  observer.observe(document.body, { childList: true, subtree: true });
};

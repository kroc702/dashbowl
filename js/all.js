
const GITHUB_REPO = "kroc702/dashbowl";
const BRANCH = "main";
const DOCS_DIR = "";
// Détermine automatiquement le nom de la page depuis l'URL
let path = window.location.pathname.replace(/^\/|\/$/g, '');
console.log('{{ site.baseurl }}');
if (!path || path.endsWith('/')) {
  path += "index";
}
// Construit l'URL vers l'éditeur de fichiers GitHub
const editUrl = `https://github.com/${GITHUB_REPO}/edit/${BRANCH}/${DOCS_DIR}${path}.md`;
// Applique le lien au bouton
document.getElementById("github-edit-link").href = editUrl;


function goToProse(repo, page) {
    window.location = repo.replace(/^https?:\/\/[^\/]*\//i,'http://prose.io/#') + '/edit/gh-pages/' + page;
}

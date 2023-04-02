class TMConfig:

    title = u'Création d’un composant web capable de générer des quiz et autres exercices éducatifs '
    first_name = 'Patrick'
    last_name = 'Oliveira Alves'
    author = f'{first_name} {last_name}'
    year = u'2023'
    month = u'Avril'
    seminary_title = u'Développement Web'
    tutor = u"Cédric Donner et Johan Jobin"
    release = ""
    repository_url = "https://github.com/PatrickUnicorn/sphinx-tm-template"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

tmconfig = TMConfig()
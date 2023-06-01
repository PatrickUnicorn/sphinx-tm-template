class DocumentInfos:

    title = u'Développement de composants Web afin de créer des quiz interactifs'
    first_name = 'Patrick'
    last_name = 'Oliveira Alves'
    address = u'Rue des Agges 46, 1635 La Tour-de-trême'
    author = f'{first_name} {last_name}'
    the_date = f'Le 2 avril 2023'
    year = u'2023'
    month = u'Avril'
    seminary_title = u'Développement Web'
    tutor = u"Cédric Donner et Johan Jobin"
    release = ""
    repository_url = "https://github.com/PatrickUnicorn/sphinx-tm-template"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year
tmconfig = DocumentInfos()
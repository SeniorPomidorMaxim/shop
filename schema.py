import graphene
from graphene_django.types  import DjangoObjectType, ObjectType
from .models import Author,Genre,Book

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author

class BookType(DjangoObjectType):
    class Meta:
        model = Book

class GenreType(DjangoObjectType):
    class Meta:
        model = Genre

# Create a Query type запрос для получения данных списком или единично
class Query(ObjectType):
    author= graphene.Field(AuthorType, id=graphene.Int())
    book = graphene.Field(BookType, id=graphene.Int())
    genre = graphene.Field(GenreType, id = graphene.Int())
    authors = graphene.List(AuthorType)
    books = graphene.List(BookType)
    genres = graphene.List(GenreType)

#функия преобразователь для Author

    def resolve_author(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Author.objects.get(pk=id)

        return None

#функия преобразователь для Book

    def resolve_book(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Book.objects.get(pk=id)

        return None

#функия преобразователь для Genre    

    def resolve_genre(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Genre.objects.get(pk=id)

        return None

    def resolve_authors(self, info, **kwargs):
        return Author.objects.all()

    def resolve_books(self, info, **kwargs):
        return Book.objects.all()
    
    def resolve_genres(self, info, **kwargs):
        return Genre.objects.all()
    
# создаем Input Object Types

class GenreInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()
    

class AuthorInput(graphene.InputObjectType):
    id = graphene.ID()
    first_name = graphene.String()
    last_name = graphene.String()


class BookInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    authors = graphene.List(AuthorInput)
    release_date = graphene.Int()
    genre = graphene.List(GenreInput)

# создание мутации для authors
class CreateAuthor(graphene.Mutation):
    class Arguments:
        input = AuthorInput(required=True)
    ok = graphene.Boolean()
    author = graphene.Field(AuthorType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        author_instance = Author(first_name=input.first_name, last_name=input.last_name)
        author_instance.save()
        return CreateAuthor(ok=ok, author=author_instance)

class UpdateAuthor(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = AuthorInput(required=True)
    ok = graphene.Boolean()
    author = graphene.Field(AuthorType)
    
    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        author_instance = Author.objects.get(pk=id)
        if author_instance:
            ok = True
            author_instance.first_name = input.first_name
            author_instance.last_name = input.last_name
            author_instance.save()
        return UpdateAuthor(ok=ok, author=author_instance)

# создание мутации для genre
class CreateGenre(graphene.Mutation):
    class Arguments:
        input = GenreInput(required=True)
    ok = graphene.Boolean()
    genre = graphene.Field(GenreType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        genre_instance = Genre(name=input.name, description=input.description)
        genre_instance.save()
        return CreateGenre(ok=ok, genre=genre_instance)

class UpdateGenre(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = GenreInput(required=True)
    ok = graphene.Boolean()
    genre = graphene.Field(GenreType)
    
    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        genre_instance = Genre.objects.get(pk=id)
        if genre_instance:
            ok = True
            genre_instance.name = input.name
            genre_instance.description = input.description
            genre_instance.save()
        return UpdateGenre(ok=ok, genre=genre_instance)


# создание мутации для book
class CreateBook(graphene.Mutation):
    class Arguments:
        input = BookInput(required=True)

    ok = graphene.Boolean()
    book = graphene.Field(BookInput)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        # логика для добавления автора
        authors = []
        genres = []
        for author_input in input.authors:
            author = Author.objects.get(pk=author_input.id)
            if author is None:
                return CreateBook(ok=False, book=None)
            authors.append(author)
        
        for genre_input in input.genres:
            genre = Genre.objects.get(pk=genre_input.id)
            if genre is None:
                return CreateBook(ok=False, book=None)
            genres.append(genre)

        book_instance = Book(
            title=input.title,
            release_date=input.release_date
        )
        book_instance.save()
        book_instance.authors.set(authors)
        book_instance.genres.set(genres)
        return CreateBook(ok=ok, book=book_instance)


class UpdateBook(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = BookInput(required=True)

    ok = graphene.Boolean()
    book = graphene.Field(BookType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        book_instance = Book.objects.get(pk=id)
        if book_instance:
            ok = True
            authors = []
            genres = []

            for author_input in input.authors:
                author = Author.objects.get(pk=author_input.id)
                if author is None:
                    return CreateBook(ok=False, book=None)
                authors.append(author)

            for genre_input in input.genres:
                genre = Genre.objects.get(pk=genre_input.id)
                if genre is None:
                    return CreateBook(ok=False, book=None)
                genres.append(genre)
        
            book_instance = Book(
                title=input.title,
                release_date=input.release_date
            )

            book_instance.save()
            book_instance.authors.set(authors)
            book_instance.genres.set(genres)
            return UpdateBook(ok=ok, book=book_instance)
        return UpdateBook(ok=ok, book=None)

class Mutation(graphene.ObjectType):
     create_author = CreateAuthor.Field()
     update_author = UpdateAuthor.Field()
     create_genre = CreateGenre.Field()
     update_genre = UpdateGenre.Field()
     create_book = CreateBook.Field() 
     update_book = UpdateBook.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

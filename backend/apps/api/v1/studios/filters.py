from ninja import Schema


class StudioFilter(Schema):
    mal_id: str = None

    # icontains based search
    #   Allowed :
    #       A1 Pictures, Studio Ghibli
    #       A1 Pictures
    name: str = None

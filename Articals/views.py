from django.shortcuts import render
import Articals.models as m
import redis
# Create your views here.


Template_Name = "index.html"


def articals_list(request):
    return render(request, Template_Name, context=get_data())


def get_artical_data(conn, key_name, key):
    name = conn.hget(key_name, key).decode("utf-8")
    return name


def get_data_from_cash(conn, lis, name_key, text_key):
    for keys in conn.hkeys(name_key):
        print(keys)
        lis['artical_list'].append(
            {
                "pk": str(keys),
                "name": get_artical_data(conn,
                                         name_key,
                                         keys),
                "text": get_artical_data(conn,
                                         text_key,
                                         keys)})


def get_data_from_database_cash(conn, lis, name_key, text_key):
    all_objects = m.Artical.objects.all()
    for objects in all_objects:
        lis['artical_list'].append({"pk": objects.pk,
                                    "name": objects.name,
                                    "text": objects.text})
        conn.hset(name_key, objects.pk, objects.name)
        conn.hset(text_key, objects.pk, objects.text)


def get_data_from_database(lis):
    all_objects = m.Artical.objects.all()
    for objects in all_objects:
        lis['artical_list'].append({"pk": objects.pk,
                                    "name": objects.name,
                                    "text": objects.text})


def get_data():
    redis_articals_name_key = "articals:name"
    redis_articals_text_key = "articals:text"
    conn = redis.Redis()
    lis = {"artical_list": []}
    try:
        if int(conn.hlen(redis_articals_name_key)) > 0:
            get_data_from_cash(conn, lis,
                               redis_articals_name_key,
                               redis_articals_text_key)
        else:
            get_data_from_database_cash(conn, lis,
                                        redis_articals_name_key,
                                        redis_articals_text_key)
    except Exception as e:
        print(e)
        get_data_from_database(lis)

    return lis

import random
from faker import Faker

fake = Faker()
name = fake.name()

correct_names = [{"name": "TEST_API_DKA3"}, {"name": "     "}, {"name": "_1№;%:?*)_$_"}, {"name": ""},
                 {"name": f"{name}"}]
incorrect_names = [{"": ""}, {}, {"person": f"{name}"}, {"name": 123}]

incorrect_token = "E22KX2fR7zx7EGI"
incorrect_id = "22s22"

body_meme = {
    "text": f"Вечер пятницы, утро субботы {random.randint(1, 10)}",
    "url": "https://sun9-13.userapi.com/impg/7baXWqxpMPVvxz7rmJJnV8cFs6yiO1PFsGsXRQ/aZHzlt82_fU."
           "jpg?size=929x905&quality=96&sign=5b9cf9b9b3e0f46cd9ace6b023249eef&c_uniq_tag=hnaqx8M"
           "-kYqa_hhwuzvy8dcNsizvftoC_ET1PIvZH94&type=album",
    "tags": ["friday", "relax", "Anthony Edward 'Tony' Stark"],
    "info": {"person": f"{name}"}
}

incorrect_body_meme = {
    "url": "https://sun9-13.userapi.com/impg/7baXWqxpMPVvxz7rmJJnV8cFs6yiO1PFsGsXRQ/aZHzlt82_fU."
           "jpg?size=929x905&quality=96&sign=5b9cf9b9b3e0f46cd9ace6b023249eef&c_uniq_tag=hnaqx8M"
           "-kYqa_hhwuzvy8dcNsizvftoC_ET1PIvZH94&type=album",
    "tags": ["friday", "relax", "Anthony Edward 'Tony' Stark"],
    "info": {"person": f"{name}"}
}

test_body = [{
    "text": f"Вечер пятницы, утро субботы {random.randint(1, 10)}",
    "url": "https://sun9-13.userapi.com/impg/7baXWqxpMPVvxz7rmJJnV8cFs6yiO1PFsGsXRQ/aZHzlt82_fU."
           "jpg?size=929x905&quality=96&sign=5b9cf9b9b3e0f46cd9ace6b023249eef&c_uniq_tag=hnaqx8M"
           "-kYqa_hhwuzvy8dcNsizvftoC_ET1PIvZH94&type=album",
    "tags": ["friday", "relax", "Anthony Edward 'Tony' Stark"],
    "info": {"person": f"{name}"}
}, {
    "text": "",
    "url": "https://sun9-13.userapi.com/impg/7baXWqxpMPVvxz7rmJJnV8cFs6yiO1PFsGsXRQ/aZHzlt82_fU."
           "jpg?size=929x905&quality=96&sign=5b9cf9b9b3e0f46cd9ace6b023249eef&c_uniq_tag=hnaqx8M"
           "-kYqa_hhwuzvy8dcNsizvftoC_ET1PIvZH94&type=album",
    "tags": ["friday", "relax", "Anthony Edward 'Tony' Stark"],
    "info": {"person": f"{name}"}
}, {
    "text": "   ",
    "url": "https://sun9-13.userapi.com/impg/7baXWqxpMPVvxz7rmJJnV8cFs6yiO1PFsGsXRQ/aZHzlt82_fU."
           "jpg?size=929x905&quality=96&sign=5b9cf9b9b3e0f46cd9ace6b023249eef&c_uniq_tag=hnaqx8M"
           "-kYqa_hhwuzvy8dcNsizvftoC_ET1PIvZH94&type=album",
    "tags": ["friday", "relax", "Anthony Edward 'Tony' Stark"],
    "info": {"person": f"{name}"}
},]
incorrect_boby = [{
    "text": 123,
    "url": "https://sun9-13.userapi.com/impg/7baXWqxpMPVvxz7rmJJnV8cFs6yiO1PFsGsXRQ/aZHzlt82_fU."
           "jpg?size=929x905&quality=96&sign=5b9cf9b9b3e0f46cd9ace6b023249eef&c_uniq_tag=hnaqx8M"
           "-kYqa_hhwuzvy8dcNsizvftoC_ET1PIvZH94&type=album",
    "tags": ["friday", "relax", "Anthony Edward 'Tony' Stark"],
    "info": {"person": f"{name}"}
}, {
    "text": "_!@#$% ^&*() ",
    "url": "https://sun9-13.userapi.com/impg/7baXWqxpMPVvxz7rmJJnV8cFs6yiO1PFsGsXRQ/aZHzlt82_fU."
           "jpg?size=929x905&quality=96&sign=5b9cf9b9b3e0f46cd9ace6b023249eef&c_uniq_tag=hnaqx8M"
           "-kYqa_hhwuzvy8dcNsizvftoC_ET1PIvZH94&type=album",
    "tags": ["friday", "relax", "Anthony Edward 'Tony' Stark"],
    "info": {"person": f"{name}"}
}, {
    "text": f"Вечер пятницы, утро субботы {random.randint(1, 10)}",
    "url": "",
    "tags": ["friday", "relax", "Anthony Edward 'Tony' Stark"],
    "info": {"person": f"{name}"}
}, {
    "text": f"Вечер пятницы, утро субботы {random.randint(1, 10)}",
    "url": "  ",
    "tags": ["friday", "relax", "Anthony Edward 'Tony' Stark"],
    "info": {"person": f"{name}"}
}, {
    "text": f"Вечер пятницы, утро субботы {random.randint(1, 10)}",
    "url": "_!@#$% ^&*() ",
    "tags": ["friday", "relax", "Anthony Edward 'Tony' Stark"],
    "info": {"person": f"{name}"}
}, {
    "text": f"Вечер пятницы, утро субботы {random.randint(1, 10)}",
    "url": 123,
    "tags": ["friday", "relax", "Anthony Edward 'Tony' Stark"],
    "info": {"person": f"{name}"}
}, {
    "text": f"Вечер пятницы, утро субботы {random.randint(1, 10)}",
    "url": "https://sun9-13.userapi.com/impg/7baXWqxpMPVvxz7rmJJnV8cFs6yiO1PFsGsXRQ/aZHzlt82_fU."
           "jpg?size=929x905&quality=96&sign=5b9cf9b9b3e0f46cd9ace6b023249eef&c_uniq_tag=hnaqx8M"
           "-kYqa_hhwuzvy8dcNsizvftoC_ET1PIvZH94&type=album",
    "tags": [""],
    "info": {"person": f"{name}"}
}, {
    "text": f"Вечер пятницы, утро субботы {random.randint(1, 10)}",
    "url": "https://sun9-13.userapi.com/impg/7baXWqxpMPVvxz7rmJJnV8cFs6yiO1PFsGsXRQ/aZHzlt82_fU."
           "jpg?size=929x905&quality=96&sign=5b9cf9b9b3e0f46cd9ace6b023249eef&c_uniq_tag=hnaqx8M"
           "-kYqa_hhwuzvy8dcNsizvftoC_ET1PIvZH94&type=album",
    "tags": ["   "],
    "info": {"person": f"{name}"}
}, {
    "text": f"Вечер пятницы, утро субботы {random.randint(1, 10)}",
    "url": "https://sun9-13.userapi.com/impg/7baXWqxpMPVvxz7rmJJnV8cFs6yiO1PFsGsXRQ/aZHzlt82_fU."
           "jpg?size=929x905&quality=96&sign=5b9cf9b9b3e0f46cd9ace6b023249eef&c_uniq_tag=hnaqx8M"
           "-kYqa_hhwuzvy8dcNsizvftoC_ET1PIvZH94&type=album",
    "tags": ["_!@#$% ^&*()_"],
    "info": {"person": f"{name}"}
}, {
    "text": f"Вечер пятницы, утро субботы {random.randint(1, 10)}",
    "url": "https://sun9-13.userapi.com/impg/7baXWqxpMPVvxz7rmJJnV8cFs6yiO1PFsGsXRQ/aZHzlt82_fU."
           "jpg?size=929x905&quality=96&sign=5b9cf9b9b3e0f46cd9ace6b023249eef&c_uniq_tag=hnaqx8M"
           "-kYqa_hhwuzvy8dcNsizvftoC_ET1PIvZH94&type=album",
    "tags": [123],
    "info": {"person": f"{name}"}
}, {
    "text": f"Вечер пятницы, утро субботы {random.randint(1, 10)}",
    "url": "https://sun9-13.userapi.com/impg/7baXWqxpMPVvxz7rmJJnV8cFs6yiO1PFsGsXRQ/aZHzlt82_fU."
           "jpg?size=929x905&quality=96&sign=5b9cf9b9b3e0f46cd9ace6b023249eef&c_uniq_tag=hnaqx8M"
           "-kYqa_hhwuzvy8dcNsizvftoC_ET1PIvZH94&type=album",
    "tags": 123,
    "info": {"person": f"{name}"}
}, {
    "text": f"Вечер пятницы, утро субботы {random.randint(1, 10)}",
    "url": "https://sun9-13.userapi.com/impg/7baXWqxpMPVvxz7rmJJnV8cFs6yiO1PFsGsXRQ/aZHzlt82_fU."
           "jpg?size=929x905&quality=96&sign=5b9cf9b9b3e0f46cd9ace6b023249eef&c_uniq_tag=hnaqx8M"
           "-kYqa_hhwuzvy8dcNsizvftoC_ET1PIvZH94&type=album",
    "tags": ["friday", "relax", "Anthony Edward 'Tony' Stark"],
    "info": {"person": f""}
}, {
    "text": f"Вечер пятницы, утро субботы {random.randint(1, 10)}",
    "url": "https://sun9-13.userapi.com/impg/7baXWqxpMPVvxz7rmJJnV8cFs6yiO1PFsGsXRQ/aZHzlt82_fU."
           "jpg?size=929x905&quality=96&sign=5b9cf9b9b3e0f46cd9ace6b023249eef&c_uniq_tag=hnaqx8M"
           "-kYqa_hhwuzvy8dcNsizvftoC_ET1PIvZH94&type=album",
    "tags": ["friday", "relax", "Anthony Edward 'Tony' Stark"],
    "info": {"person": f"   "}
}, {
    "text": f"Вечер пятницы, утро субботы {random.randint(1, 10)}",
    "url": "https://sun9-13.userapi.com/impg/7baXWqxpMPVvxz7rmJJnV8cFs6yiO1PFsGsXRQ/aZHzlt82_fU."
           "jpg?size=929x905&quality=96&sign=5b9cf9b9b3e0f46cd9ace6b023249eef&c_uniq_tag=hnaqx8M"
           "-kYqa_hhwuzvy8dcNsizvftoC_ET1PIvZH94&type=album",
    "tags": ["friday", "relax", "Anthony Edward 'Tony' Stark"],
    "info": {"person": 123}
}, {
    "text": f"Вечер пятницы, утро субботы {random.randint(1, 10)}",
    "url": "https://sun9-13.userapi.com/impg/7baXWqxpMPVvxz7rmJJnV8cFs6yiO1PFsGsXRQ/aZHzlt82_fU."
           "jpg?size=929x905&quality=96&sign=5b9cf9b9b3e0f46cd9ace6b023249eef&c_uniq_tag=hnaqx8M"
           "-kYqa_hhwuzvy8dcNsizvftoC_ET1PIvZH94&type=album",
    "tags": ["friday", "relax", "Anthony Edward 'Tony' Stark"],
    "info": {"person": "!@#$ %^&**()_+"}
}, {
    "text": f"Вечер пятницы, утро субботы {random.randint(1, 10)}",
    "url": "https://sun9-13.userapi.com/impg/7baXWqxpMPVvxz7rmJJnV8cFs6yiO1PFsGsXRQ/aZHzlt82_fU."
           "jpg?size=929x905&quality=96&sign=5b9cf9b9b3e0f46cd9ace6b023249eef&c_uniq_tag=hnaqx8M"
           "-kYqa_hhwuzvy8dcNsizvftoC_ET1PIvZH94&type=album",
    "tags": ["friday", "relax", "Anthony Edward 'Tony' Stark"],
    "info": 123
}]

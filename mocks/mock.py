"""
Mock data for testing the meal planner API.
Contains sample meal plans in the correct format.
"""

from models.weekOfMeals import W, D, M, I

# Sample single day (Monday) for testing
mock_output_parsed_1_day = W(
    # Monday only
    m=D(
        b=M(
            d='Mediterranean Vegetable Frittata',
            l='A hearty frittata loaded with tomatoes, bell peppers, and zucchini, seasoned with fresh herbs and baked to perfection. [Recipe Link](https://www.eatingwell.com/gallery/8033274/one-pot-vegetarian-mediterranean-diet-dinners/)'
        ),
        l=M(
            d='Grilled Eggplant with Yogurt Mint Sauce',
            l='Smoky grilled eggplant slices topped with a refreshing yogurt-mint sauce, offering a delightful blend of flavors. [Recipe Link](https://cookscrafter.com/13-light-mediterranean-dinners/)'
        ),
        d=M(
            d='Lentil and Vegetable Stew',
            l='A comforting stew featuring lentils and a variety of vegetables, simmered in a flavorful broth. [Recipe Link](https://www.eatingwell.com/gallery/8033274/one-pot-vegetarian-mediterranean-diet-dinners/)'
        )
    )
)

# Sample week of meals for testing
mock_output_parsed_7_days = W(
    # Monday
    m=D(
        b=M(
            d='Mediterranean Vegetable Frittata',
            l='A hearty frittata loaded with tomatoes, bell peppers, and zucchini, seasoned with fresh herbs and baked to perfection. [Recipe Link](https://www.eatingwell.com/gallery/8033274/one-pot-vegetarian-mediterranean-diet-dinners/)'
        ),
        l=M(
            d='Grilled Eggplant with Yogurt Mint Sauce',
            l='Smoky grilled eggplant slices topped with a refreshing yogurt-mint sauce, offering a delightful blend of flavors. [Recipe Link](https://cookscrafter.com/13-light-mediterranean-dinners/)'
        ),
        d=M(
            d='Lentil and Vegetable Stew',
            l='A comforting stew featuring lentils and a variety of vegetables, simmered in a flavorful broth. [Recipe Link](https://www.eatingwell.com/gallery/8033274/one-pot-vegetarian-mediterranean-diet-dinners/)'
        )
    ),
    # Tuesday
    t=D(
        b=M(
            d='Tomato and Cucumber Salad with Feta and Mint',
            l='A refreshing salad combining ripe tomatoes, crisp cucumbers, crumbled feta, and fresh mint, dressed in olive oil. [Recipe Link](https://justlovecooking.com/mediterranean-vegetable-recipes/)'
        ),
        l=M(
            d='Stuffed Bell Peppers with Quinoa and Feta',
            l='Colorful bell peppers stuffed with a mixture of quinoa, feta cheese, and herbs, then baked until tender. [Recipe Link](https://www.healthguidetoday.com/2025/01/22/25-vegetarian-mediterranean-diet-dinner-recipes/)'
        ),
        d=M(
            d='Sicilian Eggplant and Tomato Bake',
            l='A flavorful bake featuring layers of eggplant, tomatoes, olives, and capers, seasoned with Mediterranean herbs. [Recipe Link](https://pouringflowers.com/mediterranean-one-pan-dinners/)'
        )
    ),
    # Wednesday
    w=D(
        b=M(
            d='Lemon Herb Roasted Cauliflower',
            l='Oven-roasted cauliflower florets tossed with lemon juice, fresh herbs, and olive oil, creating a zesty side dish. [Recipe Link](https://justlovecooking.com/mediterranean-vegetable-recipes/)'
        ),
        l=M(
            d='Grilled Vegetable and Halloumi Salad',
            l='A warm salad featuring grilled vegetables and halloumi cheese, tossed with a lemon-olive oil dressing. [Recipe Link](https://www.healthguidetoday.com/2025/01/22/25-vegetarian-mediterranean-diet-dinner-recipes/)'
        ),
        d=M(
            d='Vegetable Curry',
            l='A rich and creamy curry made with a variety of vegetables and spices, served over brown rice. [Recipe Link](https://mealprepify.com/mediterranean-diet-recipes-without-fish/)'
        )
    ),
    # Thursday
    th=D(
        b=M(
            d='Mediterranean Roasted Vegetables',
            l='A medley of vegetables like zucchini, bell peppers, and tomatoes, roasted with olive oil and herbs. [Recipe Link](https://hoorahtohealth.com/mediterranean-roasted-vegetables/)'
        ),
        l=M(
            d='Chickpea Stew',
            l='A hearty stew made with chickpeas, tomatoes, and spices, simmered to perfection. [Recipe Link](https://bsacs.in/25-mediterranean-diet-recipes-for-anyone-who-doesnt-like-fish/)'
        ),
        d=M(
            d='Zucchini Noodles with Pesto',
            l='Low-carb zucchini noodles tossed with a flavorful pesto sauce, offering a light and healthy meal. [Recipe Link](https://mealprepify.com/mediterranean-diet-recipes-without-fish/)'
        )
    ),
    # Friday
    f=D(
        b=M(
            d='Roasted Mediterranean Vegetables',
            l='A colorful array of vegetables roasted with olive oil and herbs, perfect as a side dish or main. [Recipe Link](https://techiecycle.com/mediterranean-roasted-vegetable-recipe/)'
        ),
        l=M(
            d='Vegetable Moussaka with Lentils',
            l='A lighter version of the classic Greek dish, featuring layers of roasted vegetables and lentils, topped with a creamy yogurt mixture. [Recipe Link](https://lifesyearning.com/easy-mediterranean-dinner-recipes/)'
        ),
        d=M(
            d='Mediterranean Pasta Salad',
            l='A vibrant pasta salad with bell peppers, cherry tomatoes, olives, and artichoke hearts, tossed in a lemon-oregano dressing. [Recipe Link](https://bsacs.in/25-mediterranean-diet-recipes-for-anyone-who-doesnt-like-fish/)'
        )
    ),
    # Saturday
    s=D(
        b=M(
            d='Grilled Eggplant with Yogurt Mint Sauce',
            l='Smoky grilled eggplant slices topped with a refreshing yogurt-mint sauce, offering a delightful blend of flavors. [Recipe Link](https://cookscrafter.com/13-light-mediterranean-dinners/)'
        ),
        l=M(
            d='Lentil and Vegetable Stew',
            l='A comforting stew featuring lentils and a variety of vegetables, simmered in a flavorful broth. [Recipe Link](https://www.eatingwell.com/gallery/8033274/one-pot-vegetarian-mediterranean-diet-dinners/)'
        ),
        d=M(
            d='Sicilian Eggplant and Tomato Bake',
            l='A flavorful bake featuring layers of eggplant, tomatoes, olives, and capers, seasoned with Mediterranean herbs. [Recipe Link](https://pouringflowers.com/mediterranean-one-pan-dinners/)'
        )
    ),
    # Sunday
    su=D(
        b=M(
            d='Tomato and Cucumber Salad with Feta and Mint',
            l='A refreshing salad combining ripe tomatoes, crisp cucumbers, crumbled feta, and fresh mint, dressed in olive oil. [Recipe Link](https://justlovecooking.com/mediterranean-vegetable-recipes/)'
        ),
        l=M(
            d='Stuffed Bell Peppers with Quinoa and Feta',
            l='Colorful bell peppers stuffed with a mixture of quinoa, feta cheese, and herbs, then baked until tender. [Recipe Link](https://www.healthguidetoday.com/2025/01/22/25-vegetarian-mediterranean-diet-dinner-recipes/)'
        ),
        d=M(
            d='Lentil and Vegetable Stew',
            l='A comforting stew featuring lentils and a variety of vegetables, simmered in a flavorful broth. [Recipe Link](https://www.eatingwell.com/gallery/8033274/one-pot-vegetarian-mediterranean-diet-dinners/)'
        )
    )
)


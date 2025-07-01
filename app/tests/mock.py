"""
Mock data for testing the meal planner API.
"""

from app.models.weekOfMeals import W, D, M


# Sample single day (Monday) for testing
mock_output_parsed_1_day = W(
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


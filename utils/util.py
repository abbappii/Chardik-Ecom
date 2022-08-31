

class Util:

    @staticmethod
    def modify_input_for_multiple_files( image):
        dict = {}
        dict['image'] = image
        return dict
    
    @staticmethod
    def points_calculate(total):
        if total <= 1000:
            points_gained = 0.1 * total
        elif total >1000 and total <= 3000:
            points_gained = 0.3 * total
        elif total >3000 and total <= 5000:
            points_gained = 0.5 * total
        elif total >5000 and total <= 10000:
            points_gained = 0.7 * total
        else:
            points_gained = 0.8 * total
        
        return points_gained
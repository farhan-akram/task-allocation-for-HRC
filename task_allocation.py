"""
System allocates the task to human or robot based on the task complexity and resource capability
Model for task complexity is used from S. N. Samy and H. Elmaraghy, “A model for measuring products assembly complexity,” Int. J. Comput. Integr. Manuf., vol. 23, no. 11, pp. 1015–1027, 2010
"""
import sys
import json

def automatic_handling_complexity():
    print("\n*** Calculating Automatic Handling Complexity ***")

    handling_attributes = []

    print("\n*** SYMMETRY ***")
    print(f"    Rotational Part")
    print(f"        1) Symmetric")
    print(f"        2) No Symmetry")
    print(f"    Non-Rotational Part")
    print(f"        3) 180 degrees symmetry about three axes")
    print(f"        4) 180 degrees symmetry about one axis only")
    print(f"        5) No Symmetry")
    value = input("Please select symmetry ")
    if int(value) == 1:
        symmetry = 0.45
        handling_attributes.append(symmetry)
    elif int(value) == 2:
        symmetry = 1
        handling_attributes.append(symmetry)
    elif int(value) == 3:
        symmetry = 0.6
        handling_attributes.append(symmetry)
    elif int(value) == 4:
        symmetry = 0.77
        handling_attributes.append(symmetry)
    elif int(value) == 5:
        symmetry = 1
        handling_attributes.append(symmetry)
    else:
        symmetry = 0

    print("\n*** FLEXIBILITY ***")
    print(f"    1) Non-Flexible")
    print(f"    2) Flexible")
    value = input("Please select flexibility ")
    if int(value) == 1:
        flexibility = 0.67
        handling_attributes.append(flexibility)
    elif int(value) == 2:
        flexibility = 1
        handling_attributes.append(flexibility)
    else:
        flexibility = 0

    print("\n*** DELICATENESS ***")
    print(f"    1) Non-Delicate")
    print(f"    2) Delicate")
    value = input("Please select delicateness ")
    if int(value) == 1:
        delicateness = 0.8
        handling_attributes.append(delicateness)
    elif int(value) == 2:
        delicateness = 1
        handling_attributes.append(delicateness)
    else:
        delicateness = 0

    print("\n*** STICKINESS ***")
    print(f"    1) Non-Sticky")
    print(f"    2) Sticky")
    value = input("Please select stickiness ")
    if int(value) == 1:
        stickiness = 0.8
        handling_attributes.append(stickiness)
    elif int(value) == 2:
        stickiness = 1
        handling_attributes.append(stickiness)
    else:
        stickiness = 0

    print("\n*** TANGLING/NESTING ***")
    print(f"    1) Not Tangled/Nested")
    print(f"    2) Tangled/Nested")
    value = input("Please select tangling/nesting ")
    if int(value) == 1:
        tangling = 0.8
        handling_attributes.append(tangling)
    elif int(value) == 2:
        tangling = 1
        handling_attributes.append(tangling)
    else:
        tangling = 0

    sum = 0
    for i in handling_attributes:
        sum += i

    if len(handling_attributes) != 0:
        handling_complexity_factor = sum / len(handling_attributes)
    else:
        sum = 1
        handling_complexity_factor = 1

    return sum, handling_complexity_factor


def automatic_insertion_complexity():
    print("\n*** Calculating Automatic Insertion Complexity ***")

    insertion_attributes = []

    print("\n*** HANDLING DOWN AFTER INSERTION ***")
    print(f"    1) Required")
    print(f"    2) Not Required")
    value = input("Please select handling down ")
    if int(value) == 1:
        holding_down = 1
        insertion_attributes.append(holding_down)
    elif int(value) == 2:
        holding_down = 0.75
        insertion_attributes.append(holding_down)
    else:
        holding_down = 0

    print("\n*** INSERTION RESISTANCE ***")
    print(f"    1) Does Exist")
    print(f"    2) Does not Exist")
    value = input("Please select insertion resistance ")
    if int(value) == 1:
        insertion_resistance = 1
        insertion_attributes.append(insertion_resistance)
    elif int(value) == 2:
        insertion_resistance = 0.67
        insertion_attributes.append(insertion_resistance)
    else:
        insertion_resistance = 0

    print("\n*** ALIGNMENT AND POSITIONING ***")
    print(f"    1) Easy")
    print(f"    2) Not Easy")
    value = input("Please select alignment and positioning ")
    if int(value) == 1:
        alignment = 0.67
        insertion_attributes.append(alignment)
    elif int(value) == 2:
        alignment = 1
        insertion_attributes.append(alignment)
    else:
        alignment = 0

    print("\n*** MECHANICAL FASTENING METHODS ***")
    print(f"    1) Screwing or other processes")
    print(f"    2) Riveting or similar processes")
    print(f"    3) Bending or similar processes")
    value = input("Please select mechanical fastening methods ")
    if int(value) == 1:
        mechanical_fastening = 0.5
        insertion_attributes.append(mechanical_fastening)
    elif int(value) == 2:
        mechanical_fastening = 0.56
        insertion_attributes.append(mechanical_fastening)
    elif int(value) == 3:
        mechanical_fastening = 1
        insertion_attributes.append(mechanical_fastening)
    else:
        mechanical_fastening = 0

    print("\n*** NON-MECHANICAL FASTENING METHODS ***")
    print(f"    1) Chemical processes")
    print(f"    2) Additional material required")
    print(f"    3) No addition of material (friction), ...")
    value = input("Please select non-mechanical fastening methods ")
    if int(value) == 1:
        non_mechanical_fastening = 0.67
        insertion_attributes.append(non_mechanical_fastening)
    elif int(value) == 2:
        non_mechanical_fastening = 0.92
        insertion_attributes.append(non_mechanical_fastening)
    elif int(value) == 3:
        non_mechanical_fastening = 1
        insertion_attributes.append(non_mechanical_fastening)
    else:
        non_mechanical_fastening = 0

    print("\n*** INSERTION DIRECTION ***")
    print(f"    1) Straight line from above")
    print(f"    2) Straight line not from above")
    print(f"    3) Not straight line insertion")
    value = input("Please select insertion direction ")
    if int(value) == 1:
        insertion_direction = 0.5
        insertion_attributes.append(insertion_direction)
    elif int(value) == 2:
        insertion_direction = 0.54
        insertion_attributes.append(insertion_direction)
    elif int(value) == 3:
        insertion_direction = 1
        insertion_attributes.append(insertion_direction)
    else:
        insertion_direction = 0

    sum = 0
    for i in insertion_attributes:
        sum += i

    if len(insertion_attributes) != 0:
        insertion_complexity_factor = sum / len(insertion_attributes)
    else:
        sum = 1
        insertion_complexity_factor = 1

    return sum, insertion_complexity_factor


def manual_handling_complexity():
    print("\n*** Calculating Manual Handling Complexity ***")

    handling_attributes = []

    print("\n*** SYMMETRY ***")
    print(f"    Rotational Part")
    print(f"        1) Symmetric")
    print(f"        2) No Symmetry")
    print(f"    Non-Rotational Part")
    print(f"        3) 180 degrees symmetry about three axes")
    print(f"        4) 180 degrees symmetry about one axis only")
    print(f"        5) No Symmetry")
    value = input("Please select symmetry ")
    if int(value) == 1:
        symmetry = 0.7
        handling_attributes.append(symmetry)
    elif int(value) == 2:
        symmetry = 1
        handling_attributes.append(symmetry)
    elif int(value) == 3:
        symmetry = 0.84
        handling_attributes.append(symmetry)
    elif int(value) == 4:
        symmetry = 0.94
        handling_attributes.append(symmetry)
    elif int(value) == 5:
        symmetry = 1
        handling_attributes.append(symmetry)
    else:
        symmetry = 0

    print("\n*** SIZE ***")
    print(f"    1) > 15 mm")
    print(f"    2) 6 mm < size <= 15 mm")
    print(f"    3) <= 6 mm")
    value = input("Please select size ")
    if int(value) == 1:
        size = 0.74
        handling_attributes.append(size)
    elif int(value) == 2:
        size = 0.81
        handling_attributes.append(size)
    elif int(value) == 3:
        size = 1
        handling_attributes.append(size)
    else:
        size = 0

    print("\n*** THICKNESS ***")
    print(f"    1) > 2 mm")
    print(f"    2) 0.25 mm < thickness <= 2 mm")
    print(f"    3) <= 0.25 mm")
    value = input("Please select thickness ")
    if int(value) == 1:
        thickness = 0.27
        handling_attributes.append(thickness)
    elif int(value) == 2:
        thickness = 0.5
        handling_attributes.append(thickness)
    elif int(value) == 3:
        thickness = 1
        handling_attributes.append(thickness)
    else:
        thickness = 0

    print("\n*** WEIGHT ***")
    print(f"    1) < 4.5 kg (light)")
    print(f"    2) >= 4.5 kg")
    value = input("Please select weight ")
    if int(value) == 1:
        weight = 0.5
        handling_attributes.append(weight)
    elif int(value) == 2:
        weight = 1
        handling_attributes.append(weight)
    else:
        weight = 0

    print("\n*** GRASPING AND MANIPULATION ***")
    print(f"    1) Easy to Grasp and Manipulation")
    print(f"    2) Not Easy to Grasp and Manipulate")
    value = input("Please select grasping and manipulation ")
    if int(value) == 1:
        grasping = 0.91
        handling_attributes.append(grasping)
    elif int(value) == 2:
        grasping = 1
        handling_attributes.append(grasping)
    else:
        grasping = 0

    print("\n*** ASSISTANCE ***")
    print(f"    1) Using One Hand")
    print(f"    2) Using One Hand with Grasping Aids")
    print(f"    3) Using Two Hands")
    print(f"    4) Using Two Hands with Assistance")
    value = input("Please select assistance ")
    if int(value) == 1:
        assistance = 0.34
        handling_attributes.append(assistance)
    elif int(value) == 2:
        assistance = 1
        handling_attributes.append(assistance)
    elif int(value) == 3:
        assistance = 0.75
        handling_attributes.append(assistance)
    elif int(value) == 4:
        assistance = 0.57
        handling_attributes.append(assistance)
    else:
        assistance = 0

    print("\n*** NESTING AND TANGLING ***")
    print(f"    1) Parts do not nest or tangle and are not flexible")
    print(f"    2) Parts severely nest or tangle or are flexible")
    value = input("Please select nesting and tangling ")
    if int(value) == 1:
        tangling = 0.58
        handling_attributes.append(tangling)
    elif int(value) == 2:
        tangling = 1
        handling_attributes.append(tangling)
    else:
        tangling = 0

    print("\n*** OPTICAL MAGNIFICATION ***")
    print(f"    1) Not Necessary")
    print(f"    2) Necessary")
    value = input("Please select optical magnification ")
    if int(value) == 1:
        optical_magnification = 0.91
        handling_attributes.append(optical_magnification)
    elif int(value) == 2:
        optical_magnification = 1
        handling_attributes.append(optical_magnification)
    else:
        optical_magnification = 0

    sum = 0
    for i in handling_attributes:
        sum += i

    if len(handling_attributes) != 0:
        handling_complexity_factor = sum / len(handling_attributes)
    else:
        sum = 1
        handling_complexity_factor = 1

    return sum, handling_complexity_factor


def manual_insertion_complexity():
    print("\n*** Calculating Manual Insertion Complexity ***")

    insertion_attributes = []

    print("\n*** HANDLING DOWN AFTER INSERTION ***")
    print(f"    1) Required")
    print(f"    2) Not Required")
    value = input("Please select handling down ")
    if int(value) == 1:
        holding_down = 1
        insertion_attributes.append(holding_down)
    elif int(value) == 2:
        holding_down = 0.54
        insertion_attributes.append(holding_down)
    else:
        holding_down = 0

    print("\n*** ALIGNMENT AND POSITIONING ***")
    print(f"    1) Easy to Align or Position")
    print(f"    2) Not Easy to Align or Position")
    value = input("Please select alignment and positioning ")
    if int(value) == 1:
        alignment = 0.86
        insertion_attributes.append(alignment)
    elif int(value) == 2:
        alignment = 1
        insertion_attributes.append(alignment)
    else:
        alignment = 0

    print("\n*** INSERTION RESISTANCE ***")
    print(f"    1) No Resistance")
    print(f"    2) Resistance to Insertion")
    value = input("Please select insertion resistance ")
    if int(value) == 1:
        insertion_resistance = 0.87
        insertion_attributes.append(insertion_resistance)
    elif int(value) == 2:
        insertion_resistance = 1
        insertion_attributes.append(insertion_resistance)
    else:
        insertion_resistance = 0

    print("\n*** ACCESSIBILITY AND VISION ***")
    print(f"    1) No Restrictions")
    print(f"    2) Obstructed access or restricted vision")
    print(f"    3) Obstructed access and restricted vision")
    value = input("Please select accessibility and vision ")
    if int(value) == 1:
        accessibility = 0.57
        insertion_attributes.append(accessibility)
    elif int(value) == 2:
        accessibility = 0.81
        insertion_attributes.append(accessibility)
    elif int(value) == 3:
        accessibility = 1
        insertion_attributes.append(accessibility)
    else:
        accessibility = 0

    print("\n*** MECHANICAL FASTENING PROCESSES ***")
    print(f"    1) Bending or similar processes")
    print(f"    2) Riveting or similar processes")
    print(f"    3) Screw Tightening or similar processes")
    print(f"    4) Bulk Plastic Deformation")
    value = input("Please select mechanical fastening methods ")
    if int(value) == 1:
        mechanical_fastening = 0.34
        insertion_attributes.append(mechanical_fastening)
    elif int(value) == 2:
        mechanical_fastening = 0.58
        insertion_attributes.append(mechanical_fastening)
    elif int(value) == 3:
        mechanical_fastening = 0.42
        insertion_attributes.append(mechanical_fastening)
    elif int(value) == 4:
        mechanical_fastening = 1
        insertion_attributes.append(mechanical_fastening)
    else:
        mechanical_fastening = 0

    print("\n*** NON-MECHANICAL FASTENING METHODS ***")
    print(f"    1) No Additional Material Required")
    print(f"    2) Soldering Processes")
    print(f"    3) Chemical Processes")
    value = input("Please select non-mechanical fastening methods ")
    if int(value) == 1:
        non_mechanical_fastening = 0.58
        insertion_attributes.append(non_mechanical_fastening)
    elif int(value) == 2:
        non_mechanical_fastening = 0.67
        insertion_attributes.append(non_mechanical_fastening)
    elif int(value) == 3:
        non_mechanical_fastening = 1
        insertion_attributes.append(non_mechanical_fastening)
    else:
        non_mechanical_fastening = 0

    print("\n*** NON-FASTENING PROCESSES ***")
    print(f"    1) Manipulation of parts or sub-assemblies (fitting or adjusting of parts, ...)")
    print(f"    2) Other processes (liquid insertion, ...)")
    value = input("Please select non-fastening processes ")
    if int(value) == 1:
        non_fastening_process = 0.75
        insertion_attributes.append(non_fastening_process)
    elif int(value) == 2:
        non_fastening_process = 1
        insertion_attributes.append(non_fastening_process)
    else:
        non_fastening_process = 0

    sum = 0
    for i in insertion_attributes:
        sum += i

    if len(insertion_attributes) != 0:
        insertion_complexity_factor = sum / len(insertion_attributes)
    else:
        sum = 1
        insertion_complexity_factor = 1

    return sum, insertion_complexity_factor


def main():

    number_of_tasks = input("Enter the number of tasks for assigning to resources: ")
    try:
        number_of_tasks = int(number_of_tasks)
    except Exception as err:
        print("Wrong input", err)
        sys.exit(1)

    tasks_resources = {}

    for i in range(number_of_tasks):

        sum1, Ch = automatic_handling_complexity()
        sum2, Ci = automatic_insertion_complexity()

        sum1_m, Ch_m = manual_handling_complexity()
        sum2_m, Ci_m = manual_insertion_complexity()

        Cpart_a = (sum1*Ch + sum2*Ci)/(sum1+sum2)
        Cpart_m = (sum1_m * Ch_m + sum2_m * Ci_m) / (sum1_m + sum2_m)

        if Cpart_m > Cpart_a:
            print(f"\nManual Task Complexity is: {Cpart_m}")
            print(f"Automatic Task Complexity is: {Cpart_a}")
            print("Task assigned to ROBOT")
            resource_assigned = "Robot"

        else:
            print(f"\nAutomatic Task Complexity is: {Cpart_a:.3}")
            print(f"Manual Task Complexity is: {Cpart_m:.3}")
            print(f"Task assigned to HUMAN")
            resource_assigned = "Human"

        task_number = "Task " + str(i+1)
        tasks_resources[task_number] = {
            "status": "ready",
            "can be done by": resource_assigned,
            "completed": "False",
            "completed by": "None",
            "start time": "None",
            "completion time": "None",
            "worker note":""
        }

    with open('tasks_resources.json', 'w') as fp:
        json.dump(tasks_resources, fp, sort_keys=True, indent=4)

    print()
    print("*** Assigned resources information are saved in a file of JSON format ***")


if __name__ == '__main__':
    main()

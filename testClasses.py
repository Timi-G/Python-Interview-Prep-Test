import json
from datetime import datetime

class Banking():
    def __init__(self):
        self.accounts={}
        self.history=[]

    def create(self,timeStamp:int,account_id:str)->bool:
        if account_id not in self.accounts:
            self.accounts[account_id]={"timeStamp":timeStamp,"deposit":[],"pay":[],"balance":0,"activities":0}
            return True
        # if any(account_id in acc for acc in self.accounts):
        #     return False

        # [all_timestamps,account_id,balance,all_transactions,activities,statement]
        # self.accounts+=[[[timeStamp],account_id,0,[0],0,[]]]
        # self.history+=[[timeStamp],[]]
        return False

    def deposit(self,timeStamp:int,account_id:str,amount:int)->int:
        if account_id not in self.accounts:
            return
        self.accounts[account_id]['timeStamp']=timeStamp
        self.accounts[account_id]['deposit']+=[amount]
        self.accounts[account_id]['balance'] +=amount
        return self.accounts[account_id]['balance']

        # if not any(account_id in acc for acc in self.accounts):
        #     print(f'create new account with account_id {account_id}')
        #     self.create(timeStamp, account_id)

        # for n,acc in enumerate(self.accounts):
        #     if account_id in acc:
        #         self.accounts[n][0]+=[timeStamp+1]
        #         balance=self.accounts[n][2]+amount
        #         self.accounts[n][2]=balance
        #         self.accounts[n][3]+=[amount]
        #         self.accounts[n][5]+=[f'{timeStamp} deposit({amount}) balance({self.accounts[n][2]})']
        #         self.history[0]+=[timeStamp]
        #         self.history[1]+=[f'deposit({account_id})']
        #         return balance

    def pay(self,timeStamp:int, account_id:str, amount:int) -> bool:
        if account_id in self.accounts:
            self.accounts[account_id]['timeStamp']=timeStamp
            if self.accounts[account_id]['balance']>=amount:
                self.accounts[account_id]['pay']+=[amount]
                self.accounts[account_id]['balance']-=amount
                return True
        return False
        # if not any(account_id in acc for acc in self.accounts):
        #     return False
        #
        # for n,acc in enumerate(self.accounts):
            # if account_id in acc:
            #     balance = self.accounts[n][2] - amount
            #     if balance < 0:
            #         return False
            #
            #     self.accounts[n][0]+=[timeStamp]
            #     self.accounts[n][2]=balance
            #     self.accounts[n][3]+=[amount]
            #     self.accounts[n][5] += [f'{timeStamp} pay({amount}) balance({self.accounts[n][2]})']
            #     self.history[0] += [timeStamp]
            #     self.history[1] += [f'pay({account_id})']
            #     return True

    def top_activities(self,timeStamp:int, n:int) -> list:
        # 1
        activities=[[acc,sum(info['deposit'])+sum(info['pay'])] for acc,info in self.accounts.items()]

        # 2
        activities=[]
        for acc,info in self.accounts.items():
            self.accounts[acc]['timeStamp']=timeStamp
            activity=sum(info['deposit'])+sum(info['pay'])
            self.accounts[acc]['activities']=activity
            activities+=[[acc,activity]]

        activities.sort(reverse=True, key=lambda x: (x[1], x[0].split().sort()))
        if len(activities)>=n:
            return [f"{activities[b][0]}({activities[b][1]})" for b in range(n)]
        else:
            return [f"{a[0]}({a[1]})" for a in activities]
        # for a,acc in enumerate(self.accounts):
        #     activity=sum(abs(am) for am in acc[3])
        #     self.accounts[a][4]=activity

        # top=self.accounts.sort(reverse=True, key=lambda x:(x[4],-int(x[1][0])))[:n]
        # top = [f"{t[1]}({t[4]})" for t in top]
        # self.history[0] += [timeStamp]
        # self.history[1] += [f'top_activities({n})']
        # return top

    def transfer(self,timeStamp:int,account_id1:str,account_id2:str,amount:int) -> bool:
        if account_id1 not in self.accounts or account_id2 not in self.accounts:
            return False

        # withdraw from sending account
        t_from=self.pay(timeStamp,account_id1,amount)
        if t_from:
            # pay to receiving account
            t_to=self.deposit(timeStamp,account_id2,amount)
            return True
        return False

    def close(self, timeStamp:int, account_id:str)->bool:
        if account_id in self.accounts:
            del self.accounts[account_id]
            return True
        return False
        # if not any(account_id in acc for acc in self.accounts):
        #     return False
        #
        # for acc in self.accounts:
        #     if account_id in acc:
        #         self.accounts.remove(acc)
        #         self.history[0] += [timeStamp]
        #         self.history[1] += [f'close({account_id})']
        #         return True

    def balance(self, timeStamp:int, account_id:str)->int|bool:
        if account_id in self.accounts:
            self.accounts[account_id]['timeStamp']=timeStamp
            return self.accounts[account_id]['balance']
        return False

    def statement(self,timeStamp:int,account_id:str)->dict:
        t=timeStamp
        acc_id=None
        balance=0
        activities=0
        if account_id in self.accounts:
            acc_id=account_id
            balance=self.accounts[account_id]['balance']
            self.accounts[account_id]['activities']=sum(self.accounts[account_id]['deposit'])+sum(self.accounts[account_id]['pay'])
            activities=self.accounts[account_id]['activities']

        return {
            'timeStamp':t,
            'account_id': acc_id,
            'balance':balance,
            'activities':activities
        }

        # for acc in self.accounts:
        #     if account_id in acc:
        #         return acc[5]

class ReviewManager:
    def __init__(self):
        self.products = {}

    def add_review(self, product_id: str, review_id: str, review_text: str, rating: int) -> bool:
        if rating < 1 or rating > 5:
            return False  # Invalid rating
        if product_id not in self.products:
            self.products[product_id] = {}
        self.products[product_id][review_id] = {"text": review_text, "rating": rating, "flagged": False}
        return True

    def get_review(self, product_id: str, review_id: str) -> dict | None:
        if product_id in self.products and review_id in self.products[product_id]:
            review = self.products[product_id][review_id]
            return {"text": review["text"], "rating": review["rating"], "flagged": review["flagged"]}
        return None

    def delete_review(self, product_id: str, review_id: str) -> bool:
        if product_id in self.products and review_id in self.products[product_id]:
            del self.products[product_id][review_id]
            if not self.products[product_id]:
                del self.products[product_id]  # Remove product if no reviews left
            return True
        return False

# Instantiate the ReviewManager
review_manager = ReviewManager()

# Adding some reviews
review_manager.add_review("p1", "r1", "Great product!", 5)
review_manager.add_review("p1", "r2", "Not bad", 3)

# Testing get_review method
print(review_manager.get_review("p1", "r1"))  # Expected: {"text": "Great product!", "rating": 5, "flagged": false}
print(review_manager.get_review("p1", "r3"))  # Expected: None

# Testing delete_review method
print(review_manager.delete_review("p1", "r2"))  # Expected: True
print(review_manager.get_review("p1", "r2"))  # Expected: None


class UserManager:

    def __init__(self):
        self.users = {}

    def add_user(self, user_id: str, name: str) -> bool:
        if user_id in self.users:
            return False
        self.users[user_id] = {"name": name}
        return True

    def get_user(self, user_id: str) -> dict | None:
        return self.users.get(user_id, None)

    def delete_user(self, user_id: str) -> bool:
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False

    def add_activity(self, user_id: str, activity: str) -> bool:
        if user_id in self.users:
            if "activities" in self.users[user_id]:
                self.users[user_id]["activities"] += [activity]
            else:
                self.users[user_id]["activities"] = [activity]
            return True
        return False

    def get_activities(self, user_id: str) -> list[str] | None:
        if user_id in self.users and "activities" in self.users[user_id]:
            return self.users[user_id]["activities"]
        return None

    def top_n_users_by_activities(self, n: int) -> list[dict]:
        users = []
        if not self.users:
            return

        for user, act in self.users.items():
            if 'activities' in act:
                activities = len(act['activities'])
            else:
                activities = 0
            users.append({'user_id': user, 'name': act['name'], 'activity_count': activities})
        users.sort(reverse=True, key=lambda x: (x['activity_count'], x['user_id'].split().sort()))

        if n <= len(users):
            return users[:n]
        return users


from datetime import datetime


class ActivityTracker:
    def __init__(self):
        self.activities = {}

    def log_activity(self, user_id: str, activity_id: str, activity_type: str, timestamp: str, details: str) -> bool:
        if user_id not in self.activities:
            self.activities[user_id] = {}
        self.activities[user_id][activity_id] = {
            "type": activity_type,
            "timestamp": timestamp,
            "details": details
        }
        return True

    def get_activity(self, user_id: str, activity_id: str) -> dict | None:
        return self.activities.get(user_id, {}).get(activity_id, None)

    def delete_activity(self, user_id: str, activity_id: str) -> bool:
        if user_id in self.activities and activity_id in self.activities[user_id]:
            del self.activities[user_id][activity_id]
            if not self.activities[user_id]:
                del self.activities[user_id]
            return True
        return False

    def aggregate_statistics(self, user_id: str) -> dict | None:
        if user_id not in self.activities:
            return

        total_activities = 0
        activity_types = {}
        times = []
        for user in self.activities[user_id].values():
            if user:
                total_activities += 1
                if user["type"] in activity_types:
                    activity_types[user["type"]] += 1
                else:
                    activity_types[user["type"]] = 1
                times += [user['timestamp']]
        earliest = times[0]
        latest = times[0]

        for t in times[1:]:
            if datetime.fromisoformat(t) < datetime.fromisoformat(earliest):
                earliest = t
            if datetime.fromisoformat(t) > datetime.fromisoformat(latest):
                latest = t
        timespan = [earliest, latest]
        return {
            "total_activities": total_activities,
            "activity_types": activity_types,
            "timespan": timespan
        }

    def get_activities_in_timespan(self, user_id: str, start_date: str, end_date: str) -> dict | None:
        start = datetime.fromisoformat(start_date)
        end = datetime.fromisoformat(end_date)
        total_activities = 0
        dates = {}

        if user_id not in self.activities or not self.activities[user_id]:
            return None

        for value in self.activities[user_id].values():
            if datetime.fromisoformat(value['timestamp']) >= start and datetime.fromisoformat(
                    value['timestamp']) <= end:
                total_activities += 1
                a_date = datetime.fromisoformat(value['timestamp']).date()
                if a_date in dates:
                    dates[a_date] += 1
                else:
                    dates[a_date] = 1
        average_activities = sum([d for d in dates.values()]) / len(dates)

        return {
            "total_activities": total_activities,
            "average_activities_per_day": average_activities
        }


class CourseManager:
    def __init__(self):
        self.courses = {}

    def add_course(self, course_id: str, name: str, instructor: str, duration: int) -> bool:
        if course_id in self.courses:
            return False
        self.courses[course_id] = {"name": name, "instructor": instructor, "duration": duration}
        return True

    def get_course(self, course_id: str) -> dict[str, str | int] | None:
        return self.courses.get(course_id, None)

    def update_course(self, course_id: str, name: str | None, instructor: str | None, duration: int | None) -> bool:
        if course_id not in self.courses:
            return False
        if name is not None:
            self.courses[course_id]["name"] = name
        if instructor is not None:
            self.courses[course_id]["instructor"] = instructor
        if duration is not None:
            self.courses[course_id]["duration"] = duration
        return True

    def filter_courses(self, min_duration: int | None, max_duration: int | None, instructor: str | None) -> list[str]:
        min_filter = dict(
            filter(lambda x: x[1]['duration'] >= min_duration, self.courses.items())) if min_duration else self.courses
        max_filter = dict(
            filter(lambda x: x[1]['duration'] <= max_duration, min_filter.items())) if max_duration else min_filter
        instructor_filter = dict(
            filter(lambda x: x[1]['instructor'] == instructor, max_filter.items())) if instructor else max_filter

        return [c for c in instructor_filter.keys()]

    def aggregate_stats(self) -> dict[str, int | float]:
        total_courses = len(self.courses)

        durations = [c.get('duration', 0) for c in self.courses.values()]
        total_duration = sum(durations)
        average_duration = total_duration / len(durations) if total_duration else 0

        return {
            'total_courses': total_courses,
            'average_duration': average_duration
        }

# Example usage
cm = CourseManager()
print(cm.add_course("C101", "Python Basics", "Alice", 20))  # True
print(cm.add_course("C102", "Java Fundamentals", "Bob", 25))  # True
print(cm.add_course("C101", "Python Advanced", "Alice", 30))  # False
print(cm.get_course("C101"))  # {"name": "Python Basics", "instructor": "Alice", "duration": 20}
print(cm.update_course("C101", "Advanced Python", None, None))  # True
print(cm.update_course("C103", "Data Science", "Charlie", 40))  # False


class UserManagementSystem:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id: str, username: str, email: str) -> None:
        self.users[user_id] = {'username': username, 'email': email}

    def get_user(self, user_id: str) -> dict[str, str] | None:
        return self.users.get(user_id)

    def delete_user(self, user_id: str) -> bool:
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False

    def aggregate_users(self, field: str, value: str) -> int:
        users = dict(filter(lambda x: x[1][field] == value, self.users.items()))
        return len(users)

    def format_users(self, format_type: str = "json") -> str:
        if format_type == "json":
            json_result = {
                "users": [{"user_id": uid, "username": info["username"], "email": info["email"]} for uid, info in
                          self.users.items()]}
            return json.dumps(json_result)

        csv_result = 'user_id,username,email'
        for uid, info in self.users.items():
            f = ','.join([uid, info['username'], info['email']])
            csv_result = csv_result + f"\n{f}"

        return csv_result


class Gradebook:
    def __init__(self):
        self.grades = {}

    def add_grade(self, student_id: str, subject: str, grade: float) -> None:
        if student_id not in self.grades:
            self.grades[student_id] = {}
        self.grades[student_id][subject] = grade

    def get_grade(self, student_id: str, subject: str) -> float | None:
        return self.grades.get(student_id, {}).get(subject)

    def delete_grade(self, student_id: str, subject: str) -> bool:
        if student_id in self.grades and subject in self.grades[student_id]:
            del self.grades[student_id][subject]
            if not self.grades[student_id]:  # Remove student_id entry if empty
                del self.grades[student_id]
            return True
        return False

    def get_statistics(self) -> dict:
        number_of_students = len(self.grades)
        grades = [v for subject in self.grades.values() for v in list(subject.values())]
        highest_grade = max(grades) if grades else None
        lowest_grade = min(grades) if grades else None
        average_grade = sum(grades) / len(grades) if grades else None

        return {
            "number_of_students": number_of_students,
            "average_grade": average_grade,
            "highest_grade": highest_grade,
            "lowest_grade": lowest_grade
        }

    def format_as_csv(self) -> str:
        csv_result = ""
        for s, subject in self.grades.items():
            for k, v in subject.items():
                result = ",".join([s, str(k), str(v)])
                csv_result += result + "\n"

        statistics = self.get_statistics()
        csv_result += ",".join([str(info) for info in statistics.values()])
        return csv_result


class TemperatureTracker:
    def __init__(self):
        self.temperatures = {}

    def add_temperature(self, city: str, temp: float) -> None:
        city = city.lower()
        if city not in self.temperatures:
            self.temperatures[city] = []
        self.temperatures[city].append(temp)

    def get_temperatures(self, city: str) -> list[float]:
        city = city.lower()
        if city in self.temperatures:
            return self.temperatures[city]
        return []

    def delete_temperatures(self, city: str) -> bool:
        city = city.lower()
        if city in self.temperatures:
            del self.temperatures[city]
            return True
        return False

    def average_temperature(self, city: str) -> float | None:
        city = city.lower()
        if city not in self.temperatures:
            return

        city_temp = self.temperatures[city]
        avg = sum(city_temp) / len(city_temp) if city_temp else None
        return avg

    def format_all_temperatures(self, min_temp: float = float('-inf')) -> str:
        filtered_data = {c: [t for t in temp if t >= min_temp] for c, temp in self.temperatures.items() if
                         any(t >= min_temp for t in temp)}
        projected_data = [{"city": c, "temperatures": temp} for c, temp in filtered_data.items()]

        total_cities = len(filtered_data)
        total_records = sum([len(temp) for temp in filtered_data.values()])

        return json.dumps(
            {"cities": projected_data, "statistics": {"total_cities": total_cities, "total_records": total_records}})

if __name__=="__main__":
    bank = Banking()


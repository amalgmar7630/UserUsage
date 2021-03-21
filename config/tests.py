from datetime import datetime, timezone, timedelta

from rest_framework import status
from rest_framework.test import APITestCase


class UsageTestCase(APITestCase):
    register_url = "/auth/signup/"
    login_url = "/auth/login/"
    post_usage_type_url = "/usage_types/"
    post_usage_current_user_url = "/users/currentUserUsages/"
    post_usage_user = "/usage/"
    get_usage_user = "/usage/"

    # Sign Up information
    sign_up_data = {
        "email": "test@example.com",
        "username": "test_user",
        "password1": "verysecure",
        "password2": "verysecure",
    }
    sign_up_data_1 = {
        "email": "tes1@example.com",
        "username": "test_user1",
        "password1": "verysecure",
        "password2": "verysecure",
    }
    usage_type_data = {
        "name": "co2",
        "unit": "ton"
    }
    usage_type_data2 = {
        "name": "o2",
        "unit": "ton"
    }
    usage_current_user_data = {
        "usage_type": 1,
    }

    def test_usage_flow_without_authentification(self):
        response_get_current_user_usages = self.client.get(self.post_usage_current_user_url,
                                                           format="json")
        # expected response
        self.assertEqual(response_get_current_user_usages.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_current_user_usage(self):
        # Signup to get the authentication token
        response_signup = self.client.post(self.register_url, self.sign_up_data, format="json")
        # expected response
        self.assertEqual(response_signup.status_code, status.HTTP_201_CREATED)
        # expected token in response json object
        self.assertTrue("token" in response_signup.json())
        token = response_signup.json()["token"]
        # expected user object in response json object
        self.assertTrue("user" in response_signup.json())
        user = response_signup.json()["user"]
        # expected id in user object
        self.assertTrue("pk" in user)
        user_pk = user["pk"]

        # Test the usage flow after Sign Up

        # set token in the header
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

        # post usage type
        response_post_user_type = self.client.post(self.post_usage_type_url, self.usage_type_data, format="json")
        # expected response
        self.assertEqual(response_post_user_type.status_code, status.HTTP_201_CREATED)
        self.assertTrue("id" in response_post_user_type.json())
        usage_type_id = response_post_user_type.json()["id"]

        # post usage type2
        response_post_user_type2 = self.client.post(self.post_usage_type_url, self.usage_type_data2, format="json")
        # expected response
        self.assertEqual(response_post_user_type2.status_code, status.HTTP_201_CREATED)
        self.assertTrue("id" in response_post_user_type2.json())
        usage_type_id2 = response_post_user_type2.json()["id"]

        # Post usage for current user
        today_datetime = datetime.now(timezone.utc).strftime("%Y-%m-%dT00:00")
        usage_current_user_data = {
            "usage_type": usage_type_id,
            "usage_at": today_datetime
        }
        response_post_current_user_usage = self.client.post(self.post_usage_current_user_url, usage_current_user_data,
                                                            format="json")
        # expected response
        self.assertEqual(response_post_current_user_usage.status_code, status.HTTP_201_CREATED)

        # Signup user 2 to get the authentication token
        response_signup1 = self.client.post(self.register_url, self.sign_up_data_1, format="json")
        # expected response
        self.assertEqual(response_signup1.status_code, status.HTTP_201_CREATED)
        # expected token in response json object
        self.assertTrue("token" in response_signup1.json())
        # expected user object in response json object
        self.assertTrue("user" in response_signup1.json())
        user1 = response_signup1.json()["user"]
        # expected id in user object
        self.assertTrue("pk" in user1)
        user_pk1 = user1["pk"]

        # Post usage for current user
        date_tomorrow = datetime.strptime(today_datetime, "%Y-%m-%dT00:00") + timedelta(days=1)
        usage_user_data = {
            "user": user_pk1,
            "usage_type": usage_type_id2,
            "usage_at": date_tomorrow
        }
        response_post_user_usage = self.client.post(self.post_usage_user, usage_user_data,
                                                    format="json")
        # expected response
        self.assertEqual(response_post_user_usage.status_code, status.HTTP_201_CREATED)

        # Get usages
        response_get_usages = self.client.get(self.get_usage_user,
                                              format="json")
        # expected response
        self.assertEqual(response_get_usages.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_get_usages.json()), 2)
        self.assertEqual(response_get_usages.json()[0]['user_id'], user_pk)
        self.assertEqual(response_get_usages.json()[1]['user_id'], user_pk1)
        usage_current_user = response_get_usages.json()[0]['id']

        # edit usage for current user
        updated_current_user_usage_data = {
            "usage_type": 2
        }
        response_edit_current_user_usage = self.client.patch(
            self.post_usage_current_user_url + str(usage_current_user) + '/',
            updated_current_user_usage_data,
            format="json")
        # expected response
        self.assertEqual(response_edit_current_user_usage.status_code, status.HTTP_200_OK)

        # delete usage for current user
        response_delete_current_user_usage = self.client.delete(
            self.post_usage_current_user_url + str(usage_current_user) + '/',
            format="json")

        # expected response
        self.assertEqual(response_delete_current_user_usage.status_code, status.HTTP_204_NO_CONTENT)

        # Get usages
        response_get_usages = self.client.get(self.get_usage_user,
                                              format="json")
        # expected response
        self.assertEqual(response_get_usages.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_get_usages.json()), 1)

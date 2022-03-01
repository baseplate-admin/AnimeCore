import { baseUrl } from "./baseUrl";

/*
    User Logour Page endpoint
    Example = 127.0.0.1:8000/authentication/logout/
*/
export const logoutPageUrl = `${baseUrl}/_authentication/logout/`;

/*
    User Signup Page endpoint
    Example = http://127.0.0.1:8000/authentication/register/
*/

export const signupPageUrl = `${baseUrl}/_authentication/register/`;

/* 
    User Edit Info Page 
    Example = http://127.0.0.1:8000/edit/user_info/
*/
export const userEditInfoPageUrl = `${baseUrl}/edit/user_info/`;

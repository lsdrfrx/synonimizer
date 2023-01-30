import { FormEvent, useState } from "react";
import { INewUserInput, IUserInput } from "../../models/user";
import { AuthType } from "../../types/authtype";

// @ts-ignore
import * as bcrypt from "bcryptjs";

import axios from "axios";
import { useCookies } from "react-cookie";

interface Props {
  type: AuthType;
}

export default function Auth({ type }: Props) {
  const [login, setLogin] = useState("");
  const [password, setPassword] = useState("");
  const [repeatPassword, setRepeatPassword] = useState("");
  const [email, setEmail] = useState("");
  const [_, setCookie] = useCookies(["access-token"]);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();

    const salt = bcrypt.genSaltSync(10);
    if (type === AuthType.SignUp) {
      const user: INewUserInput = {
        login: login,
        password: bcrypt.hashSync(password, salt),
        email: email,
      };

      const response = await axios.post(
        "http://localhost:8000/auth/signup",
        user
      );

      const data: unknown = response.headers.getAuthorization;
      if (!data) throw new Error("Unable to get authorization header");

      const token = (data as string).split(" ")[1];
      setCookie("access-token", token);
    } else if (type === AuthType.SignIn) {
      const user: IUserInput = {
        login: login,
        password: bcrypt.hashSync(password, salt),
      };

      const response = await axios.post(
        "http://localhost:8000/auth/signin",
        user
      );

      const data: unknown = response.headers.getAuthorization;
      if (!data) throw new Error("Unable to get authorization header");

      const token = (data as string).split(" ")[1];
      setCookie("access-token", token);
    }
  }

  return (
    <div className="bg-red-500 container mx-auto h-screen flex items-center">
      <div className="mx-auto w-96 h-1/2 bg-blue-500 text-center flex items-center">
        <div className="flex flex-col mx-auto">
          <p>Регистрация</p>
          <form onSubmit={handleSubmit}>
            {type === AuthType.SignUp && (
              <input
                placeholder="E-Mail"
                value={email}
                onChange={(event) => setEmail(event.target.value)}
              />
            )}
            <input
              placeholder="Логин"
              value={login}
              onChange={(event) => {
                setLogin(event.target.value);
              }}
            />
            <input
              placeholder="Пароль"
              value={password}
              onChange={(event) => {
                setPassword(event.target.value);
              }}
            />
            {type === AuthType.SignUp && (
              <input
                placeholder="Повторите пароль"
                value={repeatPassword}
                onChange={(event) => setRepeatPassword(event.target.value)}
              />
            )}
            <input type="submit" />
          </form>
        </div>
      </div>
    </div>
  );
}

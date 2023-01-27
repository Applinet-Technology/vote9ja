

import { useForm } from "react-hook-form";

import { FaBeer } from "@react-icons/all-files/fa/FaBeer";
class Question extends React.Component {
  render() {
    return <h3> Lets go for a <FaBeer />? </h3>
  }
}

import { FaBeer } from 'react-icons/fa';
class Question extends React.Component {
  render() {
    return <h3> Lets go for a <FaBeer />? </h3>
  }
}




const Example = () => {
  const { handleSubmit, register, formState: { errors } } = useForm();
  const onSubmit = values => console.log(values);

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input
        type="email"
        {...register("email", {
          required: "Required",
          pattern: {
            value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i,
            message: "invalid email address"
          }
        })}
      />
      {errors.email && errors.email.message}

      <input
        {...register("username", {
          validate: value => value !== "admin" || "Nice try!"
        })}
      />
      {errors.username && errors.username.message}

      <button type="submit">Submit</button>
    </form>
  );
};

export default Example
import { useState } from "react";
import './App.css';

function App() {

  const initialValues = { username: "", password: ""};
  const [formValues, setFormValues] = useState(initialValues)
  const [formErrors, setFormErrors] = useState({})


  //ここムズイ格納の仕方
  const handleChange = (e) => {
    // console.log(e.target.value);
    const { name, value } = e.target;
    setFormValues({ ...formValues, [name]: value });
    console.log(formValues);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    //ログイン情報を送信する処理を書く
    //バリデーションチェックをする
    setFormErrors(validate(formValues));
  }

  const validate = (values) => {
    const errors = {};

    if (!values.username) {
      errors.username = "ユーザー名を入力してください";
    }
    if (!values.password) {
      errors.password = "パスワードを入力してください";
    } else if (values.password.length < 4){
      errors.password = "4文字以上15文字以下のパスワードを入力してください";
    } else if (values.password.length > 15){
      errors.password = "4文字以上15文字以下のパスワードを入力してください";
    }
    return errors;
  };

  return (
    <div className="formContainer">
      <form onSubmit={(e) => handleSubmit(e)}>
        <h1>ログインフォーム</h1>
        <hr />
        <div className="uiForm">

          <div className="formField">
            <label>ユーザー名</label>
            <input type="text" placeholder="ユーザー名" name="username" 
            onChange={(e) => handleChange(e)}/>
          </div>
          <p className="errorMsg">{formErrors.username}</p>

          <div className="formField">
            <label>パスワード</label>
            <input type="text" placeholder="パスワード" name="password"
            onChange={(e) => handleChange(e)}/>
          </div>
          <p className="errorMsg">{formErrors.password}</p>

          <button className="submitButton">ログイン</button>
        </div>
      </form>
    </div>      
  );
}

export default App;

package com.example.loginappas

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val email = findViewById<EditText>(R.id.editTextEmail).text
        val pass = findViewById<EditText>(R.id.editTextPass).text
        val passConf = findViewById<EditText>(R.id.editTextPassConf).text
        val alert = findViewById<TextView>(R.id.textViewAlert)
        val confirm = findViewById<Button>(R.id.buttonConfirm)

        confirm.setOnClickListener{
            if (!email.contains("@")){
                alert.text = "Nieprawidłowy adres e-mail"
            } else if (pass != passConf){
                alert.text = "Hasła się różnią"
            } else{
                alert.text = "Witaj, ${email}"
            }
        }
    }
}
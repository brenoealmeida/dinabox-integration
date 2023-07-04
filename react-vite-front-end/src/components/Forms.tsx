import { useState } from 'react';

function Forms() {
  const [markUps, setMarkUps] = useState({
    mkpMdfBranco: 0,
    mkpMdfMadeirado: 0,
    mkpMdfEspecial: 0,
    mkpFerrBasicas: 0,
    mkpFerrEspeciais: 0,
    mkpAcessorios: 0,
    mkpPerfisPux: 0,
  });

  function resetForm() {
    setMarkUps({
      mkpMdfBranco: 0,
      mkpMdfMadeirado: 0,
      mkpMdfEspecial: 0,
      mkpFerrBasicas: 0,
      mkpFerrEspeciais: 0,
      mkpAcessorios: 0,
      mkpPerfisPux: 0,
    });
  }

  function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    return event.target;
  }

  function handleMkpChange(
    event: React.ChangeEvent<
    HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement
    >,
  ) {
    const { name, value } = event.target;
    setMarkUps({
      ...markUps,
      [name]: value,
    });
  }

  return (
    <div>
      <div>
        <form onSubmit={ handleSubmit }>
          <label>
            <br />
            Mark-Up MDF Branco:
            <input
              required
              name="mkpMdfBranco"
              value={ markUps.mkpMdfBranco }
              onChange={ handleMkpChange }
            />
          </label>
          <label>
            <br />
            <br />
            Mark-Up MDF Madeirado:
            <input
              required
              name="mkpMdfMadeirado"
              value={ markUps.mkpMdfMadeirado }
              onChange={ handleMkpChange }
            />
          </label>
          <label>
            <br />
            <br />
            Mark-Up MDF Especial:
            <input
              required
              name="mkpMdfEspecial"
              value={ markUps.mkpMdfEspecial }
              onChange={ handleMkpChange }
            />
          </label>
          <label>
            <br />
            <br />
            Mark-Up Ferragens Básicas:
            <input
              required
              name="mkpFerrBasicas"
              value={ markUps.mkpFerrBasicas }
              onChange={ handleMkpChange }
            />
          </label>
          <label>
            <br />
            <br />
            Mark-Up Ferragens Especiais:
            <input
              required
              name="mkpFerrEspeciais"
              value={ markUps.mkpFerrEspeciais }
              onChange={ handleMkpChange }
            />
          </label>
          <label>
            <br />
            <br />
            Mark-Up Acessórios:
            <input
              required
              name="mkpAcessorios"
              value={ markUps.mkpAcessorios }
              onChange={ handleMkpChange }
            />
          </label>
          <label>
            <br />
            <br />
            Mark-Up Perfis e Puxadores:
            <input
              required
              name="mkpPerfisPux"
              value={ markUps.mkpPerfisPux }
              onChange={ handleMkpChange }
            />
          </label>
        </form>
      </div>
    </div>
  );
}

export default Forms;

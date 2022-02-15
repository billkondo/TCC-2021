import { Grid, Link, Typography } from '@mui/material';
import {
  MONOGRAFIA_URL,
  NAME,
  PROJECT_URL,
  SUPERVISOR_NAME,
  SUPERVISOR_URL,
} from './constants';
import TextFieldsIcon from '@mui/icons-material/TextFields';
import GitHubIcon from '@mui/icons-material/GitHub';

import IconLink from './components/IconLink';

function App() {
  return (
    <Grid container style={{ padding: 16, height: '100%' }} direction="column">
      <Grid item container justifyContent="center">
        <Grid item xs={10} sm={7} lg={4}>
          <Typography variant="h4" style={{ fontFamily: 'Fredoka One' }}>
            MAC0499 - Trabalho de Formatura
          </Typography>
        </Grid>
      </Grid>

      <Grid
        item
        container
        justifyContent="center"
        style={{ marginTop: 24, lineHeight: 1.5 }}
      >
        <Grid item xs={10} sm={7} lg={4}>
          <Typography variant="body1" style={{ textAlign: 'justify' }}>
            <span style={{ fontFamily: 'Fredoka One' }}>Contagem distinta</span>{' '}
            é o problema de se encontrar o número de elementos distintos em um
            fluxo de dados com repetições de elementos. A solução trivial, que
            insere os dados em uma tabela, tem um consumo de espaço linear e é
            inviável para aplicações com alto volume de dados. Algoritmos
            probabilísticos resolvem esse problema trocando a exatidão da
            contagem por uma grande redução do consumo de espaço. Então, este
            trabalho apresentará soluções probabilísticas para a contagem
            distinta.
          </Typography>
        </Grid>
      </Grid>

      <Grid item container justifyContent="center" style={{ marginTop: 16 }}>
        <Grid item xs={10} sm={7} lg={4}>
          <Typography
            variant="body2"
            style={{ fontFamily: 'Pacifico', textAlign: 'end' }}
          >
            {NAME}
          </Typography>
        </Grid>
      </Grid>

      <Grid item container justifyContent="center" style={{ marginTop: 8 }}>
        <Grid item xs={10} sm={7} lg={4}>
          <Link
            href={SUPERVISOR_URL}
            underline="hover"
            target="_blank"
            rel="noopener"
          >
            <Typography
              variant="body2"
              style={{ fontFamily: 'Fredoka One', textAlign: 'end' }}
            >
              {SUPERVISOR_NAME}{' '}
              <span style={{ fontFamily: 'Roboto' }}>(Supervisor)</span>
            </Typography>
          </Link>
        </Grid>
      </Grid>

      <Grid
        item
        container
        justifyContent="center"
        alignContent="center"
        style={{ marginTop: 16, flexGrow: 1 }}
      >
        <Grid
          item
          xs={12}
          sm={7}
          lg={4}
          container
          justifyContent="center"
          spacing={5}
        >
          <Grid item>
            <IconLink
              icon={<TextFieldsIcon />}
              text="Monografia"
              url={MONOGRAFIA_URL}
            />
          </Grid>

          <Grid item>
            <IconLink icon={<GitHubIcon />} text="Projeto" url={PROJECT_URL} />
          </Grid>
        </Grid>
      </Grid>
    </Grid>
  );
}

export default App;

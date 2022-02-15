import { Typography, IconButton, Grid, Link } from '@mui/material';

const IconLink = ({ text, icon, url }) => {
  return (
    <Grid container direction="column" justifyContent="center">
      <Grid item container justifyContent="center" style={{ color: '#1976d2' }}>
        {icon}
      </Grid>

      <Grid item>
        <Link underline="hover" href={url} target="_blank" rel="noopener">
          <Typography variant="body2" style={{ fontFamily: 'Fredoka One' }}>
            {text}
          </Typography>
        </Link>
      </Grid>
    </Grid>
  );
};

export default IconLink;

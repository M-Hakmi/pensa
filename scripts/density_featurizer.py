from pensa.features import \
    read_water_features, \
    read_atom_features


"""
For the PDB visualisation, the trajectory needs to be fit to the first frame of the simulation
so that the density and protein align with each other.

Get the water pocket data for the top 3 most probable sites (top_waters = 3).
Orientation of the waters (spherical coordinates [radians]) is a timeseries distribution.
When water is not present at the site, the orientation is recorded as 10000.0 to represent an empty state.

Visualise the pocket occupancies on the reference structure in a pdb file (write=True) with occupation frequencies
saved as b_factors. If write=True, you must specify the water model for writing out the grid.

Options include:
 - SPC
 - TIP3P
 - TIP4P
 - water

  """

struc = "mor-data/11426_dyn_151.pdb"
xtc = "mor-data/11423_trj_151.xtc"
water_feat, water_data = read_water_features(
    structure_input=struc,
    xtc_input=xtc,
    top_waters=1,
    atomgroup="OH2",
    write_grid_as="TIP3P",
    out_name="11426_dyn_151"
)


# # We can use the get_atom_features, which provides the same
# # functionality but ignores orientations as atoms are considered spherically symmetric.

struc = "mor-data/11426_dyn_151.pdb"

xtc = "mor-data/11423_trj_151.xtc"

# # Here we locate the sodium site which has the highest probability
# # The density grid is written (write=True) using the default density conversion "Angstrom^{-3}" in MDAnalysis

atom_feat, atom_data = read_atom_features(
    structure_input=struc,
    xtc_input=xtc,
    top_atoms=1,
    atomgroup="SOD",
    element="Na",
    out_name="11426_dyn_151"
)


# If we have already obtained the grid, we can speed up featurization by reading it in.

struc = "mor-data/11426_dyn_151.pdb"
xtc = "mor-data/11423_trj_151.xtc"
grid = "11426_dyn_151_OH2_density.dx"
water_feat, water_data = read_water_features(
    structure_input=struc,
    xtc_input=xtc,
    top_waters=5,
    atomgroup="OH2",
    grid_input=grid
)

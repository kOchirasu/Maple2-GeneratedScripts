using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004261: Ludaritz Palace
/// </summary>
public class _11004261 : NpcScript {
    internal _11004261(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0911203207011173$ 
                // - <font color="#909090">(There's a placard in front of the palace.)</font>
                //   <i>There exists on Karkar Island two grand mansions that the Aliba Foundation has invested in. $map:02010062$ is one of them.</i>
                return true;
            case 10:
                // $script:0911203207011174$ 
                // - <font color="#909090">(There's a placard in front of the palace.)</font>
                //   <i>There exists on Karkar Island two grand mansions that the Aliba Foundation has invested in. $map:02010062$ is one of them.</i>
                // $script:0911203207011175$ 
                // - <i>This mansion features a wondrous garden and other amenities. Only those with the express permission of the Aliba Foundation can live here, regardless of wealth or social stature.</i>
                // $script:0911203207011176$ 
                // - <i>For a time, it became a popular tourist destination, with a cafe on the first floor and the terrace opened to the public. However, due to fans swarming the building anytime $npc:11000406[gender:0]$ visited for some much-deserved rest and relaxation, the house has now been closed to the public.</i>
                return true;
            default:
                return true;
        }
    }
}

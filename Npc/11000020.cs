using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000020: Marina
/// </summary>
public class _11000020 : NpcScript {
    internal _11000020(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000101$ 
                // - How may I help you?
                return true;
            case 30:
                // $script:0831180407000104$ 
                // - I still can't believe that the road to $map:02000001$ is out. All the supplies for the empress's court have been sent along that road. Do you think anyone fell in when the ground opened up? Yeesh.
                return true;
            case 40:
                // $script:0831180407000105$ 
                // - The open court of the empress is just around the corner, and yet bad things are happening constantly around here. First the supply carriage was robbed, and then the earthquake happened. All I wanted was for all this to go smoothly.
                return true;
            default:
                return true;
        }
    }
}

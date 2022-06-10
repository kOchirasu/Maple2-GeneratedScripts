using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004221: Agent S
/// </summary>
public class _11004221 : NpcScript {
    internal _11004221(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806222707010788$ 
                // - I can't really talk right now. 
                return true;
            case 10:
                // $script:0806222707010789$ 
                // - Can't talk, secret mission. I told $npc:11004220[gender:0]$ to meet right here by the balloons. Where is he? You don't think <i>they</i> got to him first, do you...? 
                return true;
            default:
                return true;
        }
    }
}

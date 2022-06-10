using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000552: Blackstar Gangster
/// </summary>
public class _11000552 : NpcScript {
    internal _11000552(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002337$ 
                // - What seems to be the problem? 
                return true;
            case 10:
                // $script:0831180407002338$ 
                // - If you've got business here, talk to a broker. Keep your hands to yourself. I'll be watching. 
                return true;
            default:
                return true;
        }
    }
}

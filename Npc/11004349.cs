using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004349: Bobo
/// </summary>
public class _11004349 : NpcScript {
    internal _11004349(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109213607011761$ 
                // - Ha, you like Bobo's red nose? Remind you of someone? 
                return true;
            case 10:
                // $script:1109213607011762$ 
                // - Ha, you like Bobo's red nose? Remind you of someone? 
                return true;
            default:
                return true;
        }
    }
}

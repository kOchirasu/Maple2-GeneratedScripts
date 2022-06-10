using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004161: Nurse Nora
/// </summary>
public class _11004161 : NpcScript {
    internal _11004161(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0730132107010547$ 
                // - Are you here to see the doctor? Do you have an appointment?
                return true;
            case 10:
                // $script:0730132107010548$ 
                // - Sigh, no time to rest. Too many patients to get to.
                return true;
            default:
                return true;
        }
    }
}

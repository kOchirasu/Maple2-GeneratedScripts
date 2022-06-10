using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001853: Dr. Henry
/// </summary>
public class _11001853 : NpcScript {
    internal _11001853(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1020165907007321$ 
                // - I'm glad you're all right.
                return true;
            case 30:
                // $script:1020165907007322$ 
                // - I'm glad you've made a quick recovery.  Come and see me whenever you're hurt. You can pop in for a checkup in the hospital lobby, just outside the patient rooms. 
                return true;
            default:
                return true;
        }
    }
}

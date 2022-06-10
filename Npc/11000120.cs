using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000120: 
/// </summary>
public class _11000120 : NpcScript {
    internal _11000120(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000519$ 
                // - Select a thread.
                return true;
            case 10:
                // $script:0831180407000520$ 
                // - This road is fraught with danger. You will need to make a detour.
                //   - Voice of experience
                return true;
            default:
                return true;
        }
    }
}

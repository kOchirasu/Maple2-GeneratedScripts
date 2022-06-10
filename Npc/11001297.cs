using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001297: Tara
/// </summary>
public class _11001297 : NpcScript {
    internal _11001297(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1215203907005011$ 
                // - I can't stand this...
                return true;
            case 40:
                // $script:1227194507005641$ 
                // - If nobody stands up to injustice, then we all suffer.
                // $script:1227194507005642$ 
                // - Just because others turn a blind eye, that doesn't mean that <i>we</i> should. If something is wrong, then we must work to make it right.
                // $script:1227194507005643$ 
                // - Otherwise, it all becomes a vicious cycle. People like us need to act or nothing will ever change.
                return true;
            default:
                return true;
        }
    }
}

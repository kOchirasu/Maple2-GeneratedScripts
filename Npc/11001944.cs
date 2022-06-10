using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001944: Guitar Student
/// </summary>
public class _11001944 : NpcScript {
    internal _11001944(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1123165007007490$ 
                // - Can I help you?
                return true;
            case 30:
                // $script:1208184307007530$ 
                // - I hear there's a lot of top talent here for the audition. I'm a little worried...
                return true;
            default:
                return true;
        }
    }
}

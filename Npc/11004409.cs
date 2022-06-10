using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004409: Condor
/// </summary>
public class _11004409 : NpcScript {
    internal _11004409(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1113161307011835$ 
                // - Back in my day, we knew a thing or two about duty!
                return true;
            case 10:
                // $script:1113161307011836$ 
                // - Flying continents appearing from nowhere? Ha! This is nothing. You should've seen the crazy things that happened back in <i>my</i> day!
                return true;
            default:
                return true;
        }
    }
}

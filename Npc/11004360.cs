using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004360: Aiden
/// </summary>
public class _11004360 : NpcScript {
    internal _11004360(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109213607011771$ 
                // - Is it so much to ask that we have a normal celebration this year?
                return true;
            case 10:
                // $script:1109213607011772$ 
                // - I've got a reputation as a know-it-all, but I can't imagine why anyone would do this to our family...
                // $script:1120173007011848$ 
                // - I rely on science to explain things... but how can it explain <i>this</i>...
                switch (selection) {
                    // $script:1120173007011849$
                    // - You should focus on helping $npcName:11004345[gender:1]$ out here.
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1120173007011850$ 
                // - I'm not so sure about that, honestly.
                return true;
            default:
                return true;
        }
    }
}

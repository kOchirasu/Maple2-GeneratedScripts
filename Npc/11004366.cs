using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004366: Mia
/// </summary>
public class _11004366 : NpcScript {
    internal _11004366(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109213607011777$ 
                // - I doubt you understand the joys of a freshly-baked cake. And the holidays are the perfect time for perfect cakes!
                return true;
            case 10:
                // $script:1109213607011778$ 
                // - I do love baking, you know. It's one of my little personal joys. And there's nothing like baking for your family over the holidays.
                switch (selection) {
                    // $script:1120173007011852$
                    // - Do you like cake?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1120173007011853$ 
                // - What a ridiculous question. I <i>love</i> cake. And I love it so much that I cannot tolerate cakes that disappoint me.
                return true;
            default:
                return true;
        }
    }
}

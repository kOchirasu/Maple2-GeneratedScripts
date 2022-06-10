using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004493: Bacopa
/// </summary>
public class _11004493 : NpcScript {
    internal _11004493(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012347$ 
                // - I'm here researching the fish of Kritias.
                return true;
            case 10:
                // $script:1227192907012348$ 
                // - I'm here researching the fish of Kritias.
                switch (selection) {
                    // $script:1227192907012349$
                    // - What have you learned?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1227192907012350$ 
                // - Every fish I've caught has had trace amounts of aetherine in their systems. The amount might be related to their place in the food chain...
                // $script:1227192907012351$ 
                // - If I were to cook and eat one of these fish, would the aetherine stay in <i>my</i> system? Until I figure this out, we're going to be reliant on food rations delivered from the mainland.
                switch (selection) {
                    // $script:0114161207012703$
                    // - I hope you figure it out.
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:0114161207012704$ 
                // - So do I, my friend. So do I.
                return true;
            default:
                return true;
        }
    }
}

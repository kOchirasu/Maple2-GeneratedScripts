using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004272: Aesop
/// </summary>
public class _11004272 : NpcScript {
    internal _11004272(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0911203207011245$ 
                // - I've been duped! Everyone said this was the best vacation spot, but no one told me about the snakes!
                return true;
            case 10:
                // $script:0911203207011246$ 
                // - I've been duped! Everyone said this was the best vacation spot, but no one told me about the snakes!
                // $script:0911203207011247$ 
                // - I knew I should've done more research. But things were so busy at work...
                switch (selection) {
                    // $script:0911203207011248$
                    // - Is this place really that popular?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:0911203207011249$ 
                // - Oh, yeah, it's all the rage. Everyone talks about the treasure chests in the water, so I had to see them for myself. But... the snakes! Why are there so many snakes?
                switch (selection) {
                    // $script:0911203207011250$
                    // - Are they poisonous?
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:0911203207011251$ 
                // - Everyone says they're not, but I'm not so sure. I took out a second mortgage to afford this trip. I can't believe this is happening!
                // $script:0911203207011252$ 
                // - Forget the treasure chests... I'll be happy to get out of here alive! My vacation is ruined!!
                return true;
            default:
                return true;
        }
    }
}

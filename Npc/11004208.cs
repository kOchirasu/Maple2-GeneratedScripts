using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004208: Tumtum
/// </summary>
public class _11004208 : NpcScript {
    internal _11004208(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806045807010658$ 
                // - What is it? 
                return true;
            case 10:
                // $script:0806045807010659$ 
                // - The mush before you is merely a facsimile of his mushyness. The real $npc:11004213[gender:1]$ is actually luxuriating inside the castle. 
                switch (selection) {
                    // $script:0806045807010660$
                    // - A facsimile?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:0806045807010661$ 
                // - Fake. A fraud. A phony. See the way he bounces around? It's really just an inflatable balloon rigged up to make noises. 
                switch (selection) {
                    // $script:0806045807010662$
                    // - That's a pretty lifelike balloon.
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:0806045807010663$ 
                // - I know, right? You can touch him, if you want. Just don't pop him. These things are expensive. 
                return true;
            default:
                return true;
        }
    }
}

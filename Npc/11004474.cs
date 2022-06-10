using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004474: Wentid
/// </summary>
public class _11004474 : NpcScript {
    internal _11004474(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012151$ 
                // - Hey, do you see that huge ship? I'm not imagining it, am I?
                return true;
            case 10:
                // $script:1227192907012152$ 
                // - Hey, do you see that huge ship? I'm not imagining it, am I?
                // $script:1227192907012153$ 
                // - It's so big... How can something that big float up in the sky like that?
                switch (selection) {
                    // $script:1227192907012154$
                    // - Didn't you ride Sky Fortress to get here?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1227192907012155$ 
                // - Sure, but I couldn't exactly tell how big it is from the inside. Seeing it now, away from the buildings in Tria... It's unreal!
                // $script:1227192907012156$ 
                // - Do you know? How does it fly like that?
                switch (selection) {
                    // $script:1227192907012157$
                    // - $npcName:24100101$ would tell you it's the power of science.
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1227192907012158$ 
                // - $npcName:24100101$? Is that the name of one of the Sky Fortress big wigs? She sounds intimidating...
                return true;
            default:
                return true;
        }
    }
}

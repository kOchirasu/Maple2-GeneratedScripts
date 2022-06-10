using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000187: Maneh
/// </summary>
public class _11000187 : NpcScript {
    internal _11000187(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000818$ 
                // - What is it?
                return true;
            case 20:
                // $script:0831180407000820$ 
                // - I want nothing to do with the empress or her army. They were supposed to protect us! Instead everyone was frozen by ice elementals.
                // $script:0831180407000821$ 
                // - My granddaughter was one of the victims. If... if the empire had just done something about the shadow gate the moment it opened, my son and his wife would still be here, safe and happy with me. 
                switch (selection) {
                    // $script:0831180407000822$
                    // - What's the story with the shadow gate?
                    case 0:
                        Id = 21;
                        return false;
                }
                return true;
            case 21:
                // $script:0831180407000823$ 
                // - The Shadow Gate is the entrance to a world of demons who serve the darkness. The empire is trying to keep their evil contained.
                // $script:0831180407000824$ 
                // - But I don't know... Closing the Shadow Gate at the cost of innocent lives... Is that really the right way to protect the world?
                // $script:0831180407000825$ 
                // - My son and his wife could be still alive somewhere on the other side of the Shadow Gate. If it is closed, I'll never see them again.
                return true;
            default:
                return true;
        }
    }
}

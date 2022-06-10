using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004089: Lupicia
/// </summary>
public class _11004089 : NpcScript {
    internal _11004089(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0622133907010310$ 
                // - Ah... Peace at last...
                return true;
            case 10:
                // $script:0622133907010311$ 
                // - Ah... Peace at last...
                // $script:0622133907010312$ 
                // - Hello. Have you come here to rest, too?
                switch (selection) {
                    // $script:0622133907010313$
                    // - That's correct.
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0622133907010314$ 
                // - I see... It's quiet here, isn't it? I love it. All of the hustle and bustle of city life just melts away...
                switch (selection) {
                    // $script:0622133907010315$
                    // - You must have been through a lot.
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:0622133907010316$ 
                // - Everyone has their challenges in life, no? I love my job, but sometimes it gets to me.
                switch (selection) {
                    // $script:0622133907010317$
                    // - I hear you.
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 33:
                // $script:0622133907010318$ 
                // - I'll be here for a little while longer, just soaking in the scents of the forest. I'm going to get plenty of rest before I go back.
                switch (selection) {
                    // $script:0622133907010319$
                    // - Enjoy yourself!
                    case 0:
                        Id = 34;
                        return false;
                }
                return true;
            case 34:
                // $script:0622133907010320$ 
                // - You, too! I bet you could use the break even more than I could. Everybody needs some rest now and then.
                return true;
            default:
                return true;
        }
    }
}

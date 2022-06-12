using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004089: Lupicia
/// </summary>
public class _11004089 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0622133907010310$
    // - Ah... Peace at last...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0622133907010311$
                // - Ah... Peace at last...
                return 10;
            case (10, 1):
                // $script:0622133907010312$
                // - Hello. Have you come here to rest, too?
                switch (selection) {
                    // $script:0622133907010313$
                    // - That's correct.
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0622133907010314$
                // - I see... It's quiet here, isn't it? I love it. All of the hustle and bustle of city life just melts away...
                switch (selection) {
                    // $script:0622133907010315$
                    // - You must have been through a lot.
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:0622133907010316$
                // - Everyone has their challenges in life, no? I love my job, but sometimes it gets to me.
                switch (selection) {
                    // $script:0622133907010317$
                    // - I hear you.
                    case 0:
                        return 33;
                }
                return -1;
            case (33, 0):
                // $script:0622133907010318$
                // - I'll be here for a little while longer, just soaking in the scents of the forest. I'm going to get plenty of rest before I go back.
                switch (selection) {
                    // $script:0622133907010319$
                    // - Enjoy yourself!
                    case 0:
                        return 34;
                }
                return -1;
            case (34, 0):
                // $script:0622133907010320$
                // - You, too! I bet you could use the break even more than I could. Everybody needs some rest now and then.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.SelectableDistractor,
            (34, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

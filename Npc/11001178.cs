using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001178: Charky
/// </summary>
public class _11001178 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1012113807004098$
    // - You rotten swine, I won't let you get away with this!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1012113807004101$
                // - Do you know what it's like to see your life's work destroyed in a single day? Well I do! <b>I've lost my farm<b>! Gah! I'm so mad I can't even sleep at night.
                switch (selection) {
                    // $script:1012113807004102$
                    // - What happened?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1012113807004103$
                // - At first I saw them in the distance, like a tidal wave. Before I knew it, my farm was blanketed by a horde of pigs! They crashed through my farm, trampling everything, leaving only ruin! I couldn't believe my eyes...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

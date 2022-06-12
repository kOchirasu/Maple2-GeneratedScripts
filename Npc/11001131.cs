using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001131: Roteo
/// </summary>
public class _11001131 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0911192907003866$
    // - Hmm? What do you want?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0911192907003869$
                // - Hah. Cold, are we? Maybe you should've worn thicker clothes.
                switch (selection) {
                    // $script:0911192907003870$
                    // - I'm not c-c-cold.
                    case 0:
                        return 31;
                    // $script:0911192907003871$
                    // - Are you kidding? I'm <b>freezing</b>.
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:0911192907003872$
                // - Bahaha. A real tough cookie, aren't you?  I'm a professional explorer, and even I get a little cold at times like this. Maybe you belong in my line of work.
                return -1;
            case (32, 0):
                // $script:0911192907003873$
                // - You look like seasoned adventurer. I'm sure you've seen worse weather than this. So suck it up! Bahaha.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

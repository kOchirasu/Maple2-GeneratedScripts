using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001275: Branko
/// </summary>
public class _11001275 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1207123607004824$
    // - The air here is cleaner than in $map:2000270$.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1207123607004827$
                // - Yes? What do you want?
                switch (selection) {
                    // $script:1207123607004828$
                    // - I heard you're Maccan's assistant.
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1207123607004829$
                // - Yes. What of it? If you want to ask <i>why</i> I'm still working as Dr. $npcName:11001276[gender:0]$'s assistant, save your breath.
                switch (selection) {
                    // $script:1207123607004830$
                    // - Why are you sti— Oh.
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:1207123607004831$
                // - I knew it! Some people just can't open their mouths without letting a stupid question slip out.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

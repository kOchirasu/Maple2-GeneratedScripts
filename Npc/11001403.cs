using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001403: Racafony
/// </summary>
public class _11001403 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217025910001349$
    // - Let's see, what else can I do for fun around here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1223143510001425$
                // - Is there something I can do for you?
                switch (selection) {
                    // $script:1223143510001426$
                    // - I want to go to <font color="#ffd200">Victoria Island</font>.
                    case 0:
                        return 31;
                    // $script:1223143510001427$
                    // - ...
                    case 1:
                        return 34;
                }
                return -1;
            case (31, 0):
                // $script:1223143510001428$
                // - A-ha, you came to board the <i>Lumiwind</i>! Perfect timing... we're nearly done with maintenance. Did you want to depart right away?
                switch (selection) {
                    // $script:1223143510001429$
                    // - Yes.
                    case 0:
                        return 32;
                    // $script:1223143510001430$
                    // - I'll come back later.
                    case 1:
                        return 33;
                }
                return -1;
            case (32, 0):
                // functionID=1 
                // $script:1223143510001431$
                // - All right, bon voyage!
                return -1;
            case (33, 0):
                // $script:1223143510001432$
                // - Huh? So you don't want to fly? Okay. Well, let me know if you change your mind.
                return -1;
            case (34, 0):
                // $script:1223143510001433$
                // - Let me know if I can help.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Close,
            (33, 0) => NpcTalkButton.Close,
            (34, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

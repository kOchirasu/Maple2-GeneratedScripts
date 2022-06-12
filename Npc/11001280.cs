using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001280: Eupheria
/// </summary>
public class _11001280 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1208234507004843$
    // - I-I'm not... strong enough...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1208234507004846$
                // - Gah! I failed to avenge Master Arazaad. Again!
                switch (selection) {
                    // $script:1208234507004847$
                    // - You'll get your chance.
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1208234507004848$
                // - Just wait. Perhaps I'm not strong enough now, but I'll keep training. And someday, I'll rend $npcName:11001231[gender:0]$ asunder!
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

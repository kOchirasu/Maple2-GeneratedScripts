using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000257: Douglas
/// </summary>
public class _11000257 : NpcScript {
    protected override int First() {
        return 1;
    }

    // Select 0:
    // $script:0831180610000408$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (1, 0):
                // functionID=1 
                // $script:0831180610000413$
                // - Being strong is important, but looking fabulous while you fight is the true key to happiness, y'know. So... wanna spruce up your gear?
                switch (selection) {
                    // $script:0831180610000414$
                    // - Yes! I need more color in my life!
                    case 0:
                        return 0;
                }
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (1, 0) => NpcTalkButton.SelectableBeauty,
            _ => NpcTalkButton.None,
        };
    }
}

using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004461: Safehold Guardsman
/// </summary>
public class _11004461 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012070$
    // - All's well!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012071$
                // - All's well!
                return 10;
            case (10, 1):
                // $script:1227192907012072$
                // - Two months out from retirement, and I get assigned here. Just my luck.
                return 10;
            case (10, 2):
                // $script:1227192907012073$
                // - Forget justice and duty! I want to go home!
                switch (selection) {
                    // $script:1227192907012074$
                    // - Stick with it, soldier!
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1227192907012075$
                // - No way. I don't have what it takes to be a hero! I just want to go hide under my bunk!
                return 11;
            case (11, 1):
                // $script:1227192907012076$
                // - Don't tell Condor about this, by the way. If he hears I've been talking like this, I'm done for!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

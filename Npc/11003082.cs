using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003082: Chorrie
/// </summary>
public class _11003082 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0113143107007764$
    // - Sniff, sniff... Chorrie is scared... Too many evil people out there.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0113143107007767$
                // - No, no. Don't. I don't know anything. I really don't.
                switch (selection) {
                    // $script:0113143107007768$
                    // - Aww, it's okay. Take it easy.
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0113143107007769$
                // - Sob... No one knows how I feel. Why can't I be left alone? Sob...
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

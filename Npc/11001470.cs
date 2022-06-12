using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001470: Gulliver Olivieta
/// </summary>
public class _11001470 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1223040807005540$
    // - Pass me by and you'll have a hundred years of bad luck.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1223040807005543$
                // - Nice place, right? If <i>you</i> lived here, you'd never have to worry about getting caught out in the rain or snow. I was going to keep it for myself, but make your best offer and this house could be yours!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

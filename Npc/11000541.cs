using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000541: Tai
/// </summary>
public class _11000541 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0831180407002307$
    // - What's wrong?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407002309$
                // - The worst thing that can happen to anyone is losing their home. It's like having the ground ripped out from under you.
                return -1;
            case (30, 0):
                // $script:0831180407002310$
                // - An eye for an eye... I'm going to teach them what it feels like to have your life shaken to its roots.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
